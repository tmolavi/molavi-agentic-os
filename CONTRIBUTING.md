# Contributing to Molavi Agentic OS

Thank you for your interest in contributing to **Molavi Agentic OS**!

## Engineering Standards

1. **Bot-Ready Specification:** Every new agent must achieve a minimum score of **80/100** on `molavi-agentic-os validate`.
2. **Minimal Dependencies:** Core orchestration must remain runnable on pure Python 3.10+ without heavy mandatory infrastructure (like Redis or Docker).
3. **Free-First:** Features must support offline local inference (Ollama) or free-tier APIs before requiring paid models.
4. **Human-in-the-Loop:** Any action with external write side-effects must default to `L2_HUMAN_APPROVAL`.
5. **Clean Provenance:** No code may be copied without verified license compatibility and proper attribution in `THIRD_PARTY_NOTICES.md` and `SOURCES.md`.

## Local Development Workflow

```bash
git clone https://github.com/tmolavi/molavi-agentic-os.git
cd molavi-agentic-os
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -v
molavi-agentic-os validate
```
