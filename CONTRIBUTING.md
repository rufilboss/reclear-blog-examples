# Contributing to Reclear Blog Examples

Thank you for helping keep Reclear's technical examples accurate, runnable, and useful.

## Scope

Contributions should improve an existing article example or add a companion example for a Reclear Blog article. Please don't add unrelated applications, generated dependencies, vendor SDK copies, or empty example directories.

## Adding an example

1. Choose the closest category and create a descriptive `kebab-case` directory, such as `observability/opentelemetry-go-jaeger/`.
2. Add a `README.md` with the article link (or `Article: forthcoming`), purpose, tested versions, prerequisites, setup, verification, cleanup, limitations, and expected results.
3. Include everything needed to reproduce the result, such as dependency manifests, lock files, tests, example configuration, and an `.env.example` **without real secrets**.
4. Include a `Makefile` with a `validate` target that runs relevant, non-destructive, local checks. The target must exit nonzero when validation fails. It should not deploy cloud infrastructure or require credentials.
5. Add a new row to the root README index when the corresponding article is published. The article and example README should link to each other.
6. Run validation locally, then submit a pull request.

Example `Makefile` (adapt it to the language and toolchain):

```make
.PHONY: validate
validate:
	python -m pytest -q
```

Do not use this Python command unless the example actually uses Python and supplies its test dependencies.

## Local validation

Run `python3 scripts/validate_examples.py` to check repository conventions and run the validation targets of any populated example directories. If a validation target needs additional local tooling, document it in that example's README.

## Pull request expectations

- Describe what changed and link to the relevant Reclear article or YouTrack task when available.
- Include reproducible verification steps and expected output.
- Update documentation and tests alongside implementation changes.
- Explain new dependencies, required permissions, and any costs.
- Confirm the example is safe to run and no credentials or personal information are included.

At least one reviewer should reproduce the example from a clean environment before the associated article is published. Use small focused changes and avoid cross-example coupling.

## Security

Never add private keys, credentials, `.env` files, production configurations containing secrets, or proprietary data. Use placeholder values and `*.example` files. If you believe you've found a security issue, **do not publish exploit details or secrets in a public issue**; contact the Reclear maintainers privately via the contact details on [reclear.io](https://reclear.io).

## Style

Use clear file names, concise documentation, explicit versions, and deterministic commands. Avoid unrelated formatting changes in other examples. Follow the conventions of each project's language and ecosystem.
