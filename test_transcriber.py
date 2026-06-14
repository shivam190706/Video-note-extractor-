from backend.transcriber import transcribe
from backend.save_transcript import save_transcript

audio_path = "uploads/audio.webm"

transcript = transcribe(audio_path)

save_transcript(transcript)

print("Done!")