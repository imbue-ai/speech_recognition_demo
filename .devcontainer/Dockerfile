# Use Ubuntu 24.04 LTS as base image
FROM ubuntu:24.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Copy uv from official image
# See: https://docs.astral.sh/uv/guides/integration/docker/#caching
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    ca-certificates \
    python3 \
    python3-pip \
    python3-venv \
    ffmpeg \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user 'dev' with sudo access
RUN useradd -m dev \
    && echo "dev ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to dev user for subsequent operations
USER dev
WORKDIR /home/dev

# Create directories for caching with proper ownership
RUN mkdir -p /home/dev/models
ENV HF_HOME=/home/dev/models

# ============================================================================
# PYTHON & ML MODELS - Pre-warm the UV cache and download Hugging Face models
# ============================================================================

# Pre-create uv virtual environment and install dependencies
# Install dependencies first (without the project itself) to maximize layer caching
COPY --chown=dev:dev pyproject.toml uv.lock /tmp/deps/
ENV UV_PROJECT_ENVIRONMENT=/home/dev/venv
RUN cd /tmp/deps && \
    uv sync --locked --no-install-project && \
    echo "Python virtual environment created successfully at $UV_PROJECT_ENVIRONMENT"

# Pre-download Whisper-tiny model (small, fast model for demos)
RUN cd /tmp/deps && \
    uv run python -c "from transformers import pipeline; pipeline('automatic-speech-recognition', model='openai/whisper-tiny')" && \
    echo "Whisper-tiny model downloaded successfully"

# Pre-download NVIDIA Parakeet model (commented out - ~2.4GB download)
# Uncomment the lines below to include the larger, more accurate Parakeet model
# RUN cd /tmp/deps && \
#     uv pip install nemo-toolkit[asr] librosa soundfile && \
#     uv run python -c "import nemo.collections.asr as nemo_asr; nemo_asr.models.ASRModel.from_pretrained('nvidia/parakeet-tdt-0.6b-v3')" && \
#     echo "Parakeet TDT model downloaded successfully"

# Clean up temporary files
RUN rm -rf /tmp/deps

# Set working directory to the workspace mount point
WORKDIR /workspace

# Default command
CMD ["bash"]
