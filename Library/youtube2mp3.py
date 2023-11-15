%pip install pytube

from pytube import YouTube
import os

while True:
  link = input("Enter your Youtube URL")
  if link == "quit":
    break
  else:
    yt = YouTube(link)
    filepath = yt.streams.filter(only_audio = True).first().download()
    mp3filepath = filepath.replace('mp4', 'mp3')
    os.rename(filepath, mp3filepath)
