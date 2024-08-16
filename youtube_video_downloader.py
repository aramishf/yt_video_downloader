from pytube import YouTube
import os

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        print(f"Downloading video: {yt.title}")
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path where you want to save the video: ")

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    download_video(url, save_path)

if __name__ == "__main__":
    main()
