SHELL := /bin/bash
.SHELLFLAGS := -euo pipefail -c

CTX_CONFIG ?= ctx.yaml
CTX_LOCAL ?= ./.bin/ctx
CTX_INSTALL ?= ./scripts/install_ctx.sh

.PHONY: help sync run test lint format typecheck build clean quality ctx-check ctx ctx-install

help:
	@printf '%s\n' \
		'Available targets:' \
		'  sync       Install project and development dependencies with uv' \
		'  run        Run the CLI' \
		'  test       Run pytest' \
		'  lint       Run ruff check' \
		'  format     Run ruff format' \
		'  typecheck  Run mypy' \
		'  build      Build source and wheel distributions' \
		'  clean      Remove local build and tool caches' \
		'  quality    Run test, lint, typecheck, and build' \
		'  ctx-check  Verify ctx is available locally or in PATH' \
		'  ctx-install Install ctx into ./.bin via scripts/install_ctx.sh' \
		'  ctx        Stage project files and build CTX documents'

sync:
	uv sync --group dev

run:
	uv run {{ cli_name }}

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy {{ package_name }}

build:
	uv build

clean:
	rm -rf build dist .pytest_cache .ruff_cache .mypy_cache .venv *.egg-info

quality: test lint typecheck build

ctx-check:
	@set -e; \
	CTX_BIN="$(CTX_LOCAL)"; \
	if [ ! -x "$$CTX_BIN" ]; then \
	  if command -v ctx >/dev/null 2>&1; then \
	    CTX_BIN="$$(command -v ctx)"; \
	  else \
	    echo "ERROR: CTX binary not found at '$(CTX_LOCAL)' and 'ctx' is not in PATH."; \
	    if [ -f "$(CTX_INSTALL)" ]; then \
	      echo "Fix: run 'make ctx-install' (network required)"; \
	    fi; \
	    exit 1; \
	  fi; \
	fi

ctx: ctx-check
	@set -e; \
	CTX_BIN="$(CTX_LOCAL)"; \
	if [ ! -x "$$CTX_BIN" ]; then \
	  CTX_BIN="$$(command -v ctx)"; \
	fi; \
	"$$CTX_BIN" tool:run project-export --no-interaction --config-file "$(CTX_CONFIG)"; \
	"$$CTX_BIN" build --config-file "$(CTX_CONFIG)"

ctx-install:
	@set -e; \
	if [ ! -f "$(CTX_INSTALL)" ]; then \
	  echo "ERROR: install script not found at '$(CTX_INSTALL)'"; \
	  exit 1; \
	fi; \
	bash "$(CTX_INSTALL)"
