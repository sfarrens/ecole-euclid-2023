# Contributing to mycosmo

Thanks for your interest in contributing! This project is a teaching demo for a course on
Scientific Software Development, so contributions are especially welcome from anyone using it
to learn — questions, typo fixes, and small improvements are just as valuable as new features.

## Getting Started

1. Fork the repository and clone your fork.
2. Install [uv](https://docs.astral.sh/uv/) if you don't already have it.
3. Sync the development environment:

   ```bash
   uv sync --all-groups
   ```

4. Install the `pre-commit` hooks so linting runs automatically before each commit:

   ```bash
   uv run pre-commit install
   ```

## Making a Change

We follow the same Git workflow taught in the accompanying
[course slides](https://sfarrens.github.io/presentations/scientific_software_development/#/5):

1. Create a feature branch off `main`, prefixed by purpose and using kebab-case, e.g.
   `feature/add-redshift-bins`, `bugfix/fix-constants-units`, `chore/update-deps`.

   ```bash
   git checkout -b feature/your-change-here
   ```

2. Make your changes, keeping commits focused and descriptive.
3. Before pushing, make sure everything passes locally:

   ```bash
   uv run ruff format .
   uv run ruff check .
   uv run mypy src
   uv run pytest
   ```

   (`pre-commit` will also run these automatically on `git commit`.)

4. Push your branch and open a Pull Request against `main`. Please describe what the change
   does and why.
5. If you're touching `src/mycosmo`, please add or update the relevant tests in `tests/` and
   docstrings (numpydoc style) alongside the code.

## Reporting Bugs and Requesting Features

Please use the corresponding [issue template](.github/ISSUE_TEMPLATE) when opening a new issue —
it helps us understand and address the report faster.

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating, you're
expected to uphold it.
