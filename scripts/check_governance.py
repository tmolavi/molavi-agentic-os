#!/usr/bin/env python3
"""TM Open Source Standard — Automated Governance & Compliance Validator.

Usage:
    python scripts/check_governance.py [--path /path/to/repo]
"""

import os
import sys
import argparse
import re

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "MODEL-REQUIREMENTS.md",
    "CHANGELOG.md",
    "ROADMAP.md",
]

REQUIRED_LANGUAGES = [
    ("English (en)", "docs/en/README.md"),
    ("Persian (fa)", "docs/fa/README.md"),
    ("Turkish (tr)", "docs/tr/README.md"),
    ("Azerbaijani (az)", "docs/az/README.md"),
    ("Arabic (ar)", "docs/ar/README.md"),
]

SECRET_PATTERNS = [
    (re.compile(r"ghp_[A-Za-z0-9]{36}"), "GitHub Personal Access Token"),
    (re.compile(r"sk-[A-Za-z0-9]{32,}"), "OpenAI Secret Key"),
    (re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9_\-]{20,}['\"]"), "Generic Hardcoded API Key"),
]

def check_repository(root_dir: str) -> bool:
    print(f"=== Running TM Open Source Governance Check across: {root_dir} ===\n")
    errors = []
    warnings = []
    passed = []

    # 1. Required Files Check
    for f in REQUIRED_FILES:
        p = os.path.join(root_dir, f)
        if os.path.exists(p) and os.path.getsize(p) > 20:
            passed.append(f"Required file present: {f}")
        else:
            errors.append(f"Missing or empty required governance file: {f}")

    # 2. Five-Language Documentation Check
    for lang_name, rel_path in REQUIRED_LANGUAGES:
        p = os.path.join(root_dir, rel_path)
        if os.path.exists(p) and os.path.getsize(p) > 30:
            passed.append(f"Language documentation present: {lang_name} ({rel_path})")
        else:
            errors.append(f"Missing regional language documentation: {lang_name} ({rel_path})")

    # 3. Model Transparency Check
    model_req_path = os.path.join(root_dir, "MODEL-REQUIREMENTS.md")
    if os.path.exists(model_req_path):
        with open(model_req_path, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read().lower()
            if "free" in content and ("ollama" in content or "local" in content or "groq" in content):
                passed.append("MODEL-REQUIREMENTS.md discloses Free-First/Local alternatives")
            else:
                warnings.append("MODEL-REQUIREMENTS.md does not explicitly detail Free-First or Local alternatives")

    # 4. License Check
    lic_path = os.path.join(root_dir, "LICENSE")
    if os.path.exists(lic_path):
        with open(lic_path, "r", encoding="utf-8", errors="ignore") as fp:
            lic_text = fp.read()
            if "MIT" in lic_text or "Apache" in lic_text:
                passed.append("Valid permissive open-source license detected")
            else:
                warnings.append("Unrecognized license format in LICENSE file")

    # 5. Internal Relative Links Check in Markdown Files
    link_regex = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    broken_links = 0
    for r, _, files in os.walk(root_dir):
        if ".git" in r or ".venv" in r or "REPOSITORY_TEMPLATE" in r:
            continue
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(r, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as fp:
                    for line_num, line in enumerate(fp, 1):
                        for m in link_regex.finditer(line):
                            target = m.group(2).strip()
                            if target.startswith("http://") or target.startswith("https://") or target.startswith("#") or target.startswith("mailto:"):
                                continue
                            clean_target = target.split("#")[0]
                            if not clean_target:
                                continue
                            target_full = os.path.normpath(os.path.join(r, clean_target))
                            if not os.path.exists(target_full):
                                errors.append(f"Broken relative link in {os.path.relpath(file_path, root_dir)}:{line_num} -> {target}")
                                broken_links += 1

    if broken_links == 0:
        passed.append("All internal relative documentation links verified successfully")

    # 6. Secret Redaction Scan
    secrets_found = 0
    for r, _, files in os.walk(root_dir):
        if ".git" in r or ".venv" in r:
            continue
        for file in files:
            file_path = os.path.join(r, file)
            if "guardrails.py" in file:
                continue
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as fp:
                    file_content = fp.read()
                    for pattern, sec_name in SECRET_PATTERNS:
                        if pattern.search(file_content):
                            errors.append(f"CRITICAL: Potential {sec_name} detected in {os.path.relpath(file_path, root_dir)}")
                            secrets_found += 1
            except Exception:
                pass

    if secrets_found == 0:
        passed.append("Zero credentials or secret keys detected in repository")

    # Summary
    print(f"PASSED CHECKS ({len(passed)}):")
    for p in passed:
        print(f"  ✓ {p}")

    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")

    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
        print(f"\n[GOVERNANCE RESULT] FAILED: {len(errors)} errors found.")
        return False

    print(f"\n[GOVERNANCE RESULT] PASSED: 100% compliant with TM Open Source Standard.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate TM Open Source Governance Compliance")
    parser.add_argument("--path", default=os.getcwd(), help="Repository root path to inspect")
    args = parser.parse_args()

    is_compliant = check_repository(args.path)
    sys.exit(0 if is_compliant else 1)
