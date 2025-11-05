#!/usr/bin/env python3
"""
Minimal speech recognition demo using Hugging Face Transformers.
Transcribes audio files to text using Whisper models.
"""

from pathlib import Path
from typing import Optional

import typer
from transformers import pipeline

app = typer.Typer()


def transcribe_audio(audio_path: Path, model_name: str = "openai/whisper-tiny") -> str:
    """
    Transcribe an audio file to text using a Hugging Face ASR model.

    Args:
        audio_path: Path to the audio file (WAV format recommended)
        model_name: Hugging Face model identifier

    Returns:
        Transcribed text
    """
    typer.echo(f"Loading model: {model_name}")
    asr_pipeline = pipeline(
        "automatic-speech-recognition",
        model=model_name,
        device=-1,  # CPU (use 0 for GPU)
    )

    typer.echo(f"Transcribing: {audio_path}")
    result = asr_pipeline(str(audio_path))

    return result["text"].strip()


@app.command()
def main(
    audio_file: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help="Input audio file to transcribe"
    ),
    output: Optional[Path] = typer.Option(
        None,
        "--output", "-o",
        help="Output text file (default: same name as input with .txt extension)"
    ),
    model: str = typer.Option(
        "openai/whisper-tiny",
        "--model", "-m",
        help="Hugging Face model to use"
    ),
):
    """Transcribe audio files using speech recognition."""
    # Determine output path
    output_path = output or audio_file.with_suffix(".txt")

    # Transcribe
    transcript = transcribe_audio(audio_file, model)

    # Write output
    output_path.write_text(transcript + "\n")

    typer.echo(f"\nTranscript saved to: {output_path}")
    typer.echo(f"\nTranscript:\n{transcript}")


if __name__ == "__main__":
    app()
