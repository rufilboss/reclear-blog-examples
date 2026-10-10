# Reclear Blog Examples

Reproducible code and configurations accompanying technical articles published on the [Reclear Blog](https://reclear.io/blog).

This repository is a **companion library**, not a collection of production-ready applications. Each example lives in its own directory and documents the exact prerequisites, commands, and limitations needed to run it.

> **Status:** Initial repository scaffold. No article examples have been published yet.

## Find an example

| Article | Example | Technologies | Tested with |
| --- | --- | --- | --- |
| _Examples will be listed as articles are published._ | — | — | — |

When publishing an example, replace the placeholder row with a link to the **published article**, a direct link to its **folder**, the key technologies, and the tested software versions. Keep the table in article-title alphabetical order.

## Categories

| Directory | Scope |
| --- | --- |
| [`kubernetes/`](kubernetes/) | Kubernetes, containers, GitOps, networking, and cluster operations |
| [`infrastructure/`](infrastructure/) | Cloud provisioning, Terraform, OpenTofu, and platform engineering |
| [`observability/`](observability/) | Metrics, logs, traces, monitoring, and OpenTelemetry |
| [`api-engineering/`](api-engineering/) | API implementation, documentation tooling, SDKs, and webhooks |
| [`ai-agents/`](ai-agents/) | Agent integrations, RAG, tool use, and evaluation |
| [`mcp/`](mcp/) | Model Context Protocol servers, clients, and security |
| [`documentation/`](documentation/) | Documentation sites, docs-as-code workflows, and writing tooling |

## Directory conventions

Use one folder per article example: `<category>/<descriptive-kebab-case-slug>/`. Do not pre-create folders for unpublished work. Keep each example self-contained, including its dependencies, configurations, tests, and a `README.md` with:

1. Link to the associated Reclear article (once published) and an overview.
2. Prerequisites and **tested versions**, including any platform assumptions.
3. Setup and execution instructions, with an `.env.example` when configuration is needed.
4. Commands for **verification and cleanup** (especially for paid cloud resources).
5. Limitations, security implications, and known differences from production setups.

Every published runnable example must include a `Makefile` with a `validate` target; it may call language-specific linters, tests, configuration checks, or safe local verification. Avoid relying on global state or secrets. CI automatically discovers example directories and runs their validation targets.

Sample layout (not yet present):

```text
mcp/
└── python-mcp-server/
    ├── README.md
    ├── Makefile
    ├── .env.example
    ├── pyproject.toml
    ├── src/
    └── tests/
```

## Quality and security

- Never commit credentials, real tokens, private keys, `.env` files, customer data, or sensitive logs.
- Document and, where feasible, pin tested versions. Keep dependency lock files for executable projects.
- Use mock services or local validation in CI. Tests must not require paid cloud deployments or privileged credentials.
- Do not run infrastructure apply/destroy steps automatically as part of validation.
- Review pull requests for reproducibility, security, and accuracy against the published article.
- GitHub Actions currently validates the repository structure and invokes `make validate` for each example when examples exist.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution and review workflow.

## License and support

Code in this repository is licensed under the [MIT License](LICENSE). Example code is provided for educational use, **as is**, without any warranty. For problems with an example, open a GitHub issue and include the example directory, tested versions, and reproduction steps. For discussion of an article, refer to its Reclear Blog page.
