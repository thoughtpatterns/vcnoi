from python:3.13-slim-bookworm

run apt-get update         \
  && apt-get --yes install \
    build-essential        \
    cmake                  \
    ffmpeg                 \
    libcairo2-dev          \
    libpango1.0-dev        \
    pkg-config             \
  && rm -rf /var/lib/apt/lists/*

copy --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

workdir /runtime

copy pyproject.toml .

run uv pip install --system 'manim>=0.19.0' 'pillow>=11.1.0'

cmd ["python3.13"]
