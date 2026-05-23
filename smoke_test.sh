#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(pwd)"
OUT_DIR="${OUT_DIR:-_tmp_hello_project}"

rm -rf "$OUT_DIR"
UV_CACHE_DIR="$ROOT_DIR/.uv-cache" uvx copier copy --trust --defaults "$ROOT_DIR" "$OUT_DIR"

cd "$OUT_DIR"
test -d .git
test "$(git config user.email)" = "681072+cs224@users.noreply.github.com"
make sync
uv run hello-cli
uv run hello-cli --name Alice
uv run python -m hello_cli --name Alice
make test
make lint
make typecheck
make build
