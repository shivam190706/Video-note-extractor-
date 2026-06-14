from faster_whisper import WhisperModel

model = WhisperModel(
    "tiny",         # ← changed from "base"
    device="cpu"
)

def transcribe(audio_path):
    segments, info = model.transcribe(
        audio_path,
        vad_filter=True,    # ← add this
        beam_size=1         # ← add this
    )

    transcript = []

    for segment in segments:
        transcript.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text
        })

    return transcript