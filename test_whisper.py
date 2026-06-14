from faster_whisper import WhisperModel

print("Loading Whisper model...")

model = WhisperModel("base", device="cpu")

print("Whisper loaded successfully!")