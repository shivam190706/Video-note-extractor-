import yt_dlp
import os
import sys

def download_audio(url):
    os.makedirs("uploads", exist_ok=True)

    # Clean old files
    for f in os.listdir("uploads"):
        os.remove(os.path.join("uploads", f))

    # Use correct ffmpeg path based on OS
    if sys.platform == "win32":
        ffmpeg_path = r"C:\ffmpeg"
    else:
        ffmpeg_path = "/usr/bin"  # Linux (Docker)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "uploads/audio.%(ext)s",
        "ffmpeg_location": ffmpeg_path,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    files = os.listdir("uploads")
    if not files:
        raise Exception("Download failed - no file found in uploads/")

    return os.path.join("uploads", files[0])