# {{ project_name }}

{{ description }}

## Requirements

- `uv`
- Python `{{ min_python }}` managed through `uv`

## Setup

Install the requested Python toolchain and sync the development environment:

```bash
uv python install {{ min_python }}
make sync
```

All commands should be run from the repository root so `[tool.uv]` uses the repo-local cache.

## Run the CLI

```bash
uv run {{ cli_name }}
uv run {{ cli_name }} --name Alice
uv run python -m {{ package_name }} --name Alice
```

## Quality checks

```bash
make test
make lint
make typecheck
make build
```

## Optional CTX integration

Install the `ctx` binary locally into `./.bin`:

```bash
make ctx-install
```

Verify the binary is available and build CTX documents from the project sources:

```bash
make ctx-check
make ctx
```

The generated CTX artifacts are written under `.context/`.

## Dependency management

Add runtime dependencies with:

```bash
uv add <package>
```

Add development dependencies with:

```bash
uv add --group dev <package>
```
