import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, HttpUrl
from backend.downloader import download_audio
from backend.transcriber import transcribe
from backend.summarizer import generate_notes
from backend.save_notes import save_notes
from backend.save_transcript import save_transcript
from backend.generate_pdf import generate_pdf
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/app")
def serve_frontend():
    return FileResponse("index.html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    url: HttpUrl

@app.get("/")
def home():
    return {"message": "Video Note AI Running"}

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    try:
        print("STEP 1: Downloading")
        audio_path = download_audio(str(request.url))

        print("STEP 2: Transcribing")
        transcript = transcribe(audio_path)

        print("STEP 3: Generating Notes")
        notes = generate_notes(transcript)

        print("STEP 4: Saving")
        transcript_file = save_transcript(transcript)
        notes_file = save_notes(notes)
        pdf_file = generate_pdf(notes, transcript)  # ✅ generate PDF

        print("STEP 5: Done")

        return {
            "notes": notes,
            "transcript": transcript,
            "transcript_length": len(transcript),
            "transcript_file": transcript_file,
            "notes_file": notes_file,
            "pdf_file": pdf_file  # ✅ return pdf path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download-pdf")
def download_pdf(path: str):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="PDF not found")
    return FileResponse(path, media_type="application/pdf", filename="notes.pdf")

    