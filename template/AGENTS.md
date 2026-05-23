# AGENTS.md

This file is policy guidance for coding agents, especially Codex, working in this repository.

## Workflow policy

- Never use system or base Python directly for project work.
- Use `uv run python`, `uv run <tool>`, `uv sync`, `uv add`, and `uv add --group dev`.
- Run `uv` and `make` commands from the repository root so `[tool.uv] cache-dir = "./.uv-cache"`
  applies consistently.
- If a package is needed for development workflows, add it in `pyproject.toml` under the `dev`
  dependency group and use it through `uv`.
- Keep dependencies declared in `pyproject.toml`; do not use ad-hoc `pip` installs.
- Avoid ad-hoc `uv` cache overrides for normal project work; use the repo-local cache configured in
  `pyproject.toml`.
- Library code should use `logging`; CLI presentation may use `print`.

## Required post-change sequence

Run these commands after making changes:

```bash
make sync
uv run {{ cli_name }}
uv run {{ cli_name }} --name Alice
uv run python -m {{ package_name }} --name Alice
make test
make lint
make typecheck
make build
```

## CTX integration (optional)

- Optional CTX config is in `ctx.yaml`.
- Installer script is `scripts/install_ctx.sh`.
- Make targets:
  - `make ctx-check` verifies CTX availability from `./.bin/ctx` or `PATH`.
  - `make ctx-install` installs CTX locally into `./.bin`.
  - `make ctx` stages project sources into `.context/` and builds CTX documents from `ctx.yaml`.

## Permissions policy

- Standard project workflow commands are pre-authorized when they require network or sandbox
  escalation: `make sync`, `make test`, `make lint`, `make typecheck`, `make build`, `uv sync`,
  and `uv run ...`.
- `make ctx-check` and `make ctx` are also pre-authorized as optional local workflow commands.
- AGENTS.md is policy guidance only; if the environment enforces escalation, still use the
  appropriate approval mechanism.
- Use the configured repo-local `uv` cache for standard workflows instead of overriding it with an
  external cache path.

Plain language: for normal setup, run, test, lint, type-check, and build steps, proceed without
re-asking unless the command is outside the standard workflow.

## Logging

- Use Python's `logging` module for runtime output in library code instead of bare `print`.
- Keep CLI presentation user-facing; use `print` for deliberate command output and `logging` for
  diagnostics.
- Initialize logging centrally in CLI entrypoints or application setup code.
- Use module-level loggers or pass loggers consistently so warnings and milestones include enough
  context to debug failures.
