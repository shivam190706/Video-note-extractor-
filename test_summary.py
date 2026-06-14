from backend.transcriber import transcribe
from backend.summarizer import generate_notes

audio_path = "uploads/audio.webm"

transcript = transcribe(audio_path)

notes = generate_notes(transcript)

print(notes)