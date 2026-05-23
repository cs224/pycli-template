# Python CLI Copier Template

This repository is a Copier template for a minimal Python CLI project with a strict `uv`-firstworkflow.
Generated projects use `hatchling` and keep the `uv` cache inside the repo.

Generate a project into a sibling directory:

```bash
UV_CACHE_DIR="$(pwd)/.uv-cache" uvx copier copy --trust . ../my-cli
```

Generate a project with defaults into a temporary directory:

```bash
UV_CACHE_DIR="$(pwd)/.uv-cache" uvx copier copy --trust --defaults . ./_tmp_hello_project
```

Generated projects are automatically initialized as git repositories and get a repo-local
`user.email` set from the `git_user_email` Copier answer. The default is
`681072+cs224@users.noreply.github.com`.

Override that email from the Copier command line:

```bash
UV_CACHE_DIR="$(pwd)/.uv-cache" uvx copier copy --trust -d git_user_email=you@example.com . ../my-cli
```

Run the smoke test for the template:

```bash
bash smoke_test.sh
```
