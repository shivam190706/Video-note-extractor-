import os
from datetime import datetime

def save_transcript(transcript):
    os.makedirs("outputs", exist_ok=True)  # ✅ create folder if missing

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/transcript_{timestamp}.txt"  # ✅ unique filename

    try:
        with open(filename, "w", encoding="utf-8") as f:
            for segment in transcript:
                start = round(segment["start"], 2)
                text = segment["text"]
                f.write(f"[{start}] {text}\n")

        print(f"Transcript saved to {filename}")
        return filename  # ✅ return path so main.py knows where it was saved

    except Exception as e:
        print(f"Failed to save transcript: {e}")
        raise