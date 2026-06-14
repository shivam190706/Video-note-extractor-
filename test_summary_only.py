from backend.summarizer import generate_notes

transcript = [
    {
        "start": 0,
        "text": "Today we are discussing artificial intelligence and machine learning."
    }
]

notes = generate_notes(transcript)

print(notes)