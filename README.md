# Python CLI Copier Template

This repository is a Copier template for a minimal Python CLI project with a strict `uv`-first workflow.
Generated projects use `hatchling`, keep the `uv` cache inside the repo, initialize git automatically, and set a repo-local git email during generation.

## Install uv (one-time setup)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Add `uv` to your `PATH` if needed, then install Python 3.12 with `uv`:

```bash
uv python install 3.12 --default
```

## Generate a new project

From the GitHub repo, with no local checkout required:

```bash
uvx copier copy --trust "gh:cs224/pycli-template" <dest>
```

Use defaults from the GitHub repo:

```bash
uvx copier copy --trust --defaults "gh:cs224/pycli-template" ./_tmp_hello_project
```

The local-path examples below only work after cloning or checking out this template repository on
disk.

Generate a project into a sibling directory from a local checkout:

```bash
UV_CACHE_DIR="$(pwd)/.uv-cache" uvx copier copy --trust . ../my-cli
```

Generate a project with defaults from a local checkout:

```bash
UV_CACHE_DIR="$(pwd)/.uv-cache" uvx copier copy --trust --defaults . ./_tmp_hello_project
```

For local-checkout usage, setting `UV_CACHE_DIR="$(pwd)/.uv-cache"` keeps Copier's `uv` cache in this template repo.
For remote `gh:...` usage, there is no template checkout-local cache to bind to, so the examples above omit `UV_CACHE_DIR`.

Generated projects are automatically initialized as git repositories and get a repo-local `user.email` set from the `git_user_email` Copier answer.
The default is `681072+cs224@users.noreply.github.com`.

## Passing parameters on the command line

Use `-d KEY=VALUE` to override defaults. Missing values fall back to template defaults.
Derived defaults are computed from the provided values, so `-d project_name=my-cli` will result in `package_name=my_cli` unless you override it explicitly.

Override a few values, including the git email:

```bash
uvx copier copy --trust "gh:cs224/pycli-template" <dest> -d project_name=my-cli -d git_user_email=you@example.com
```

Provide all template parameters explicitly:

```bash
uvx copier copy --trust "gh:cs224/pycli-template" <dest> \
  -d project_name=my-cli \
  -d package_name=my_cli \
  -d cli_name=my-cli \
  -d description="My CLI" \
  -d git_user_email=you@example.com \
  -d author_name="Your Name" \
  -d author_email=you@example.com \
  -d repo_slug="your-org/my-cli" \
  -d min_python=3.12 \
  -d license=Apache-2.0
```

## Optional persistent Copier install

If you scaffold projects frequently, you can install Copier once:

```bash
uv tool install copier
```

Then use it directly:

```bash
copier copy --trust "gh:cs224/pycli-template" <dest>
```

Run the smoke test for the template:

```bash
bash smoke_test.sh
```
