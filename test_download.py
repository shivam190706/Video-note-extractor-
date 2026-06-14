from backend.downloader import download_audio

url = input("Enter YouTube URL: ")

path = download_audio(url)

print("Downloaded:", path)