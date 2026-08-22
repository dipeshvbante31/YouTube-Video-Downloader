import yt_dlp


def download_video(url):
    options = {
        "format": "best[ext=mp4]/best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            print("Starting download...")
            ydl.download([url])
            print("Download completed!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    download_video(url)
