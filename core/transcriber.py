import os
import whisper
import numpy as np
import librosa

def transcribe_audio(audio_path: str) -> str:
    try:
        if not os.path.exists(audio_path):
            return "Error: Audio file missing."

        audio, sr = librosa.load(audio_path, sr=16000, mono=True)
        duration = len(audio) / 16000
        print(f"[DEBUG] Audio duration: {duration:.2f} seconds")

        model = whisper.load_model("base")
        result = model.transcribe(audio, fp16=False)
        return result["text"].strip()

    except Exception as e:
        return f"Transcription failed: {str(e)}"