# Speech Recognition Demo

A minimal Python project demonstrating speech recognition using Hugging Face Transformers. This project showcases:

- **UV cache pre-warming**: Dependencies are installed during container build
- **Hugging Face model pre-downloading**: Models are downloaded into the container image
- **Minimal boilerplate**: Clean, simple code structure

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

### Models Included
- **whisper-tiny** (enabled): Small, fast model for demos
- **nvidia/parakeet-tdt-0.6b-v3** (commented): Larger, more accurate model

## Usage

### In Dev Container
```bash
# Transcribe audio file
uv run transcribe test_data/OSR_us_000_0010_8k.wav

# Run tests
uv run pytest test_transcribe.py
```

### Local Installation
```bash
# Install dependencies
uv sync

# Transcribe audio
uv run transcribe test_data/OSR_us_000_0010_8k.wav -o output.txt

# Run tests
uv run pytest
```

## Testing

Uses [Syrupy](https://github.com/tophat/syrupy) for snapshot testing:
```bash
# Run test (creates snapshot on first run)
uv run pytest test_transcribe.py

# Update snapshots
uv run pytest test_transcribe.py --snapshot-update
```

## Development Container

The `.devcontainer` setup demonstrates efficient caching:

1. **Build time optimization**: Models and dependencies are downloaded during image build
2. **No runtime downloads**: Everything needed is already in the image
3. **Fast startup**: Container is ready to use immediately

To enable the Parakeet model, uncomment the lines in `.devcontainer/Dockerfile`.

## Requirements

- Python 3.11+
- UV (installed automatically in dev container)
- FFmpeg (for audio processing, included in container)
