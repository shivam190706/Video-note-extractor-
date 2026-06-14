 Video Note Extractor 

AI-powered tool that extracts structured notes from any YouTube video.

 Features
- Download audio from YouTube
-  Transcribe with Whisper AI
-  Generate notes with LLaMA3
-   Export as PDF
-  Dockerized

 Tech Stack
- FastAPI
- faster-whisper
- Ollama (LLaMA3)
- yt-dlp
- Docker

 How to Run

 Requirements
- Docker Desktop
- Ollama with llama3.2:1b installed

 Steps
1. Clone the repo
2. Run `docker-compose up`
3. Open `http://127.0.0.1:8000/app`
