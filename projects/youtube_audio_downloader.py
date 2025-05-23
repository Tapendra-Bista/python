#------------------------- audio downloader-----------------------------

from pytube import YouTube
import os

try:
    url = input("Enter YouTube video URL: ")
    yt = YouTube(url)

    print(f"Downloading audio from: {yt.title}")

    # --------------Get the best quality audio stream--------------------
    audio_stream = yt.streams.filter(only_audio=True).first()

    if audio_stream:
        # ----------------Download the audio in its original format--------------
        downloaded_file = audio_stream.download(output_path='.', filename=f"{yt.title}.webm")
        print("Download complete!")

        # Optional: Rename or convert to .mp3 if desired (requires ffmpeg)
        mp3_filename = f"{yt.title}.mp3"
        os.system(f"ffmpeg -i \"{downloaded_file}\" \"{mp3_filename}\"")
        os.remove(downloaded_file)  # Remove original file after conversion
        print("Conversion to MP3 complete!")
    else:
        print("No audio stream available for this video.")

except Exception as e:
    print(f'Something went wrong: {e}')
