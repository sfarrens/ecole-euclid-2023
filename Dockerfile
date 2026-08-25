FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

LABEL Description="MyCosmo Docker Image"
WORKDIR /home

COPY . .

RUN uv sync --frozen
