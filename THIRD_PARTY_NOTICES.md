# Third-Party Notices & Acknowledgments

All core algorithms, agent definitions, skill manifests, workflows, memory interfaces, and orchestration engines in **TM Molavi Agentic OS** are original implementations authored by **Taghi Molavi**, licensed under the **MIT License**.

This project acknowledges and appreciates the foundational contributions of the open-source AI community whose ideas informed our architectural design:

1. **Andrej Karpathy** — for [`autoresearch`](https://github.com/karpathy/autoresearch) (MIT) and [`nanochat`](https://github.com/karpathy/nanochat) (MIT), inspiring our metric-based experiment tracking, keep/revert decision engine, and minimal zero-dependency architecture.
2. **Sebastian Raschka** — for [`LLMs-from-scratch`](https://github.com/rasbt/LLMs-from-scratch) (Apache 2.0), inspiring our transparent model requirements, context boundary engineering, and technical documentation methodology.
3. **Forrest Chang** — for [`andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) (MIT), inspiring our "think before coding" behavioral directives and surgical agent execution rules.
4. **ComposioHQ** — for [`awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) (Apache 2.0), inspiring standardized `SKILL.md` portable schemas and capability discovery.
5. **Perplexity AI** — for [`bumblebee`](https://github.com/perplexityai/bumblebee) (Apache 2.0), inspiring our Bumblebee MCP security auditor, supply-chain validation, and path-traversal prevention.

---

## Python Standard Library & Optional Dev Dependencies

TM Molavi Agentic OS core relies exclusively on the **Python 3.10+ Standard Library** with zero mandatory external runtime dependencies.

Optional development and testing dependencies:
* **pytest** (MIT License) - Unit testing framework
* **pytest-cov** (MIT License) - Test coverage reporting
* **setuptools** (MIT License) - Package building utility
* **wheel** (MIT License) - Distribution archive utility

For detailed license compatibility analysis, refer to [`LICENSE_COMPATIBILITY.md`](LICENSE_COMPATIBILITY.md).
