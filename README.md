# Speech Recognition Demo

A minimal Python project demonstrating a devcontainer for speech recognition in Python.

- **UV cache pre-warming**: Dependencies are installed during container build
- **Hugging Face model pre-downloading**: Models are downloaded into the container image

## Project Structure

```
.
├── .devcontainer/          # Dev container with pre-warmed cache
│   ├── Dockerfile          # Downloads models during build
│   └── devcontainer.json   # VS Code configuration
├── test_data/              # Sample audio files
│   └── OSR_us_000_0010_8k.wav
├── transcribe.py           # Main transcription script (~85 lines)
├── test_transcribe.py      # Syrupy snapshot test (~30 lines)
└── pyproject.toml          # UV dependencies
```

## Features

### Pre-warmed Container
The Dockerfile demonstrates:
1. **UV cache pre-warming**: `uv sync` during build installs all dependencies
2. **Model pre-downloading**: Whisper-tiny model is downloaded during build
3. **Optional Parakeet model**: Commented out example for larger model (~2.4GB)

## Usage

```bash
# Transcribe audio file
uv run transcribe test_data/OSR_us_000_0010_8k.wav

# Run tests
uv run pytest test_transcribe.py
```

## Development Container

The `.devcontainer` setup demonstrates efficient caching:

1. **Build time optimization**: Models and dependencies are downloaded during image build
2. **No runtime downloads**: Everything needed is already in the image
3. **Fast startup**: Container is ready to use immediately

To enable the Parakeet model, uncomment the lines in `.devcontainer/Dockerfile`.

### Building the Docker Image

To build the Docker image locally, you can use the `devcontainer` CLI:

```bash
# Install the devcontainer CLI
npm install -g @devcontainers/cli

# Build the image
devcontainer build --workspace-folder .
```

Or use `docker build` directly:
```bash
docker build -f .devcontainer/Dockerfile .
```
