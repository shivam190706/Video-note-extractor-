import os
from datetime import datetime

def save_notes(notes):
    os.makedirs("outputs", exist_ok=True)  # ✅ create folder if missing

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/notes_{timestamp}.txt"  # ✅ unique filename

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(notes)
        print(f"Notes saved to {filename}")
        return filename  # ✅ return path so main.py knows where it was saved

    except Exception as e:
        print(f"Failed to save notes: {e}")
        raise