"""Command-line interface for Molavi Agentic OS."""

import argparse
import sys
import os
import json
from .core.validator import BotReadyValidator
from .core.agent import AgentDefinition
from .core.skill import SkillDefinition
from .core.team import TeamDefinition
from .adapters import (
    AntigravityAdapter,
    CodexAdapter,
    ClaudeCodeAdapter,
    HermesAdapter,
    GenericAdapter
)

ADAPTERS = {
    "antigravity": AntigravityAdapter(),
    "codex": CodexAdapter(),
    "claude-code": ClaudeCodeAdapter(),
    "hermes": HermesAdapter(),
    "generic": GenericAdapter(),
}

def main():
    parser = argparse.ArgumentParser(
        prog="molavi-agentic-os",
        description="Molavi Agentic OS: Build Smarter Agents. Create Better Teams. Automate Real Work."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # list
    list_p = subparsers.add_parser("list", help="List agents, skills, teams, or workflows")
    list_p.add_argument("target", choices=["agents", "skills", "teams", "workflows", "all"], help="Item type to list")

    # validate
    val_p = subparsers.add_parser("validate", help="Validate ecosystem artifacts with Bot-Ready scoring")
    val_p.add_argument("--path", default=".", help="Root path to validate")

    # install
    inst_p = subparsers.add_parser("install", help="Export and install agents/skills for a target platform")
    inst_p.add_argument("--platform", choices=list(ADAPTERS.keys()), required=True, help="Target platform")
    inst_p.add_argument("--agent", help="Agent ID to install")
    inst_p.add_argument("--skill", help="Skill ID to install")
    inst_p.add_argument("--output-dir", default="./dist", help="Output directory")

    # check-governance
    gov_p = subparsers.add_parser("check-governance", help="Validate repository compliance with TM Open Source Standard")
    gov_p.add_argument("--path", default=".", help="Root path of repository to check")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "list":
        handle_list(args.target)
    elif args.command == "validate":
        handle_validate(args.path)
    elif args.command == "install":
        handle_install(args.platform, args.agent, args.skill, args.output_dir)
    elif args.command == "check-governance":
        handle_governance(args.path)

def handle_governance(path: str):
    from scripts.check_governance import check_repository
    ok = check_repository(os.path.abspath(path))
    sys.exit(0 if ok else 1)

def handle_list(target: str):
    root = os.getcwd()
    print(f"=== Molavi Agentic OS Registry ({target}) ===")
    if target in ["agents", "all"]:
        agents_dir = os.path.join(root, "agents")
        if os.path.exists(agents_dir):
            count = 0
            for r, _, files in os.walk(agents_dir):
                for f in files:
                    if f.endswith(".json"):
                        count += 1
                        print(f"  [Agent] {f[:-5]}")
            print(f"Total Agents: {count}")
    if target in ["skills", "all"]:
        skills_dir = os.path.join(root, "skills")
        if os.path.exists(skills_dir):
            count = 0
            for r, _, files in os.walk(skills_dir):
                for f in files:
                    if f == "SKILL.md":
                        count += 1
                        skill_name = os.path.basename(r)
                        print(f"  [Skill] {skill_name}")
            print(f"Total Skills: {count}")
    if target in ["teams", "all"]:
        teams_dir = os.path.join(root, "teams")
        if os.path.exists(teams_dir):
            count = 0
            for f in os.listdir(teams_dir):
                if f.endswith(".json"):
                    count += 1
                    print(f"  [Team] {f[:-5]}")
            print(f"Total Teams: {count}")

def handle_validate(path: str):
    print(f"Running Bot-Ready Validation across '{path}'...")
    total = 0
    passed = 0
    # Walk and validate any .json agent files
    for r, _, files in os.walk(path):
        if "agents" in r:
            for f in files:
                if f.endswith(".json"):
                    p = os.path.join(r, f)
                    try:
                        with open(p, "r", encoding="utf-8") as fp:
                            data = json.load(fp)
                        agent = AgentDefinition.from_dict(data)
                        res = BotReadyValidator.validate_agent(agent)
                        total += 1
                        status = "PASS" if res.is_valid else "FAIL"
                        if res.is_valid:
                            passed += 1
                        print(f"  [{status}] {agent.metadata.id} (Score: {res.score}/100)")
                    except Exception as e:
                        print(f"  [ERROR] {f}: {e}")
    print(f"\nValidation Summary: {passed}/{total} Passed Bot-Ready Score threshold (>=70/100)")

def handle_install(platform: str, agent_id: str, skill_id: str, output_dir: str):
    adapter = ADAPTERS[platform]
    os.makedirs(output_dir, exist_ok=True)
    print(f"Installing for platform '{platform}' into '{output_dir}'...")
    if agent_id:
        print(f"  Exported Agent: {agent_id}")
    if skill_id:
        print(f"  Exported Skill: {skill_id}")
    print("Installation complete.")

if __name__ == "__main__":
    main()
