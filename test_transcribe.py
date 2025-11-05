"""
Simple syrupy snapshot test for speech recognition demo.
Tests the happy path: transcribing a sample audio file.
"""

from pathlib import Path
import pytest
from transcribe import transcribe_audio


@pytest.fixture
def sample_audio():
    """Path to the sample audio file."""
    return Path("test_data/OSR_us_000_0010_8k.wav")


def test_transcribe_sample_audio(sample_audio, snapshot):
    """
    Test transcription of sample audio file.

    This test verifies that the transcription output remains consistent.
    The first time this test runs, it will create a snapshot.
    Subsequent runs will compare against the snapshot.
    """
    assert sample_audio.exists(), f"Sample audio file not found: {sample_audio}"

    # Transcribe the audio
    transcript = transcribe_audio(sample_audio, model_name="openai/whisper-tiny")

    # Verify against snapshot
    assert transcript == snapshot
