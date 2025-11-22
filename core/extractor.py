import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio(video_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with VideoFileClip(video_path) as video:
        if video.audio is None:
            raise Exception("No audio in video.")
        video.audio.write_audiofile(output_path, logger=None)
    return output_path

def download_and_extract_audio(url, download_path="downloads"):
    from pytubefix import YouTube
    os.makedirs(download_path, exist_ok=True)
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
    video_path = os.path.join(download_path, "video.mp4")
    stream.download(output_path=download_path, filename="video.mp4")
    return extract_audio(video_path, os.path.join(download_path, "audio.wav"))