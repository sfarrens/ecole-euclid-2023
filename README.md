# Scientific Software Development Demo

[![CI](https://github.com/sfarrens/Scientific-Software-Dev-Demo/actions/workflows/ci.yml/badge.svg)](https://github.com/sfarrens/Scientific-Software-Dev-Demo/actions/workflows/ci.yml)
[![CD](https://github.com/sfarrens/Scientific-Software-Dev-Demo/actions/workflows/cd.yml/badge.svg)](https://github.com/sfarrens/Scientific-Software-Dev-Demo/actions/workflows/cd.yml)
[![Coverage](coverage.svg)](https://github.com/sfarrens/Scientific-Software-Dev-Demo/actions/workflows/cd.yml)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://sfarrens.github.io/Scientific-Software-Dev-Demo/)
[![Docker](https://img.shields.io/badge/docker-ghcr.io-blue.svg)](https://ghcr.io/sfarrens/scientific-software-dev-demo)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](https://mypy-lang.org/)

> Author: [Samuel Farrens](https://sfarrens.github.io/)
> Email: samuel.farrens@cea.fr

This repository provides a demonstration of packaging a Python code for a course on Scientific Software Development.

The slides accompanying this repository can be found [here](https://sfarrens.github.io/presentations/scientific_software_development/#/).

Example API documentation for this repository can be found [here](https://sfarrens.github.io/Scientific-Software-Dev-Demo/).

## Changelog
- 21/08/2026: The content was updated for the [2026 edition of the Rodolphe Clédassou Summer School](https://ede2026.sciencesconf.org/), based on `uv`.
- 19/08/2025: The content was updated for the [2025 edition of the Rodolphe Clédassou Summer School](https://eee2025.sciencesconf.org/)
- 02/06/2025: The content was updated for the [2025 COLOURS Programme](https://indico.ijclab.in2p3.fr/event/11110/)
- 26/08/2024: The content was updated for the [2024 edition of the Rodolphe Clédassou Summer School](https://ecole-euclid.cnrs.fr/2024-accueil/)
- 28/08/2023: The first version was made for the [2023 edition of the Euclid Summer School](https://ecole-euclid.cnrs.fr/2023-accueil/)

## Requirements

To follow this course you will need to have Python (ideally v3.12) installed. Dependency
management for this project is handled with [uv](https://docs.astral.sh/uv/).

### Core Dependencies
- python=3.12
- numpy>=1.25

### Development Dependencies (via `uv` dependency groups)
- **docs**: myst-parser, numpydoc, sphinx, sphinx-book-theme
- **lint**: mypy, pre-commit, ruff
- **profile**: line_profiler, memray, snakeviz
- **test**: pytest, pytest-cov, pytest-emoji
- **verify**: astropy

### uv install

```bash
uv sync --all-groups
```

See the [dependencies page](https://sfarrens.github.io/Scientific-Software-Dev-Demo/dependencies.html)
for how to sync individual groups.

### Manual install

All of these packages can also be installed from [PyPI](https://pypi.org/) using `pip`.

```bash
pip install numpy>=1.25 mypy pre-commit ruff myst-parser numpydoc pytest pytest-emoji pytest-cov sphinx sphinx-book-theme line_profiler memray snakeviz
```

### Docker image

You can run the code using the provided [Docker](https://www.docker.com/) image from the GitHub Container Registry. First, you'll need to authenticate with the GitHub Container Registry:

```bash
# Login to GitHub Container Registry
docker login ghcr.io
```

Then you can pull the latest image:

```bash
# Pull the latest image
docker pull ghcr.io/sfarrens/scientific-software-dev-demo:main
```

And run an interactive container:

```bash
# Run an interactive container
docker run --rm -it ghcr.io/sfarrens/scientific-software-dev-demo:main bash
```

Once inside, `uv run pytest`, `uv run python`, etc. all work exactly as they do locally.
