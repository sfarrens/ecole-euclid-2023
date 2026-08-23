# Dependencies

This page lists the mandatory dependencies required to use the `mycosmo` package.

## Core Dependencies

The following packages are required for basic usage of `mycosmo`:

- **Python** (>=3.12): The programming language used to develop the package
- **NumPy**: Required for numerical computations and array operations

## Installation

You can install the package and its core dependencies using pip:

```bash
pip install mycosmo
```

This will install the package and its core dependencies (NumPy).

## Development Dependencies

For development, `mycosmo` uses [uv](https://docs.astral.sh/uv/) and groups its
development-only dependencies into
[dependency groups](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-groups)
in `pyproject.toml`, rather than `pip` extras:

- **docs**: myst-parser, numpydoc, sphinx, sphinx-book-theme
- **lint**: mypy, pre-commit, ruff
- **profile**: line_profiler, memray, snakeviz
- **test**: pytest, pytest-cov, pytest-emoji
- **verify**: astropy

You can sync one or more of these groups with `uv sync`:

```bash
# For documentation
uv sync --group docs

# For linting and type checking
uv sync --group lint

# For profiling
uv sync --group profile

# For testing
uv sync --group test

# For verification
uv sync --group verify

# For everything at once
uv sync --all-groups
```

## Version Compatibility

The package is tested and guaranteed to work with Python 3.12 or higher. While it may work with earlier versions, these are not officially supported.
