'''
One of the best ideas to start experimenting with you hands-on python projects for students
is working on a YouTube video downloader. More than a billion people watch YouTube every month.
Sometimes there are videos we like to download permanently. YouTube doesn’t give you that option,
but you can create an app with a simple UI and the ability to download YouTube videos in different
formats and video quality. This project looks tough, but it is straightforward when you start working on it.
'''

from pytube import YouTube
from pytube import Playlist

link = input("Please enter the video url : ")
answer = input("Do you want to download one video or playlist [v/p] : ")

# print(f"The video title is : {video.title}")
# print(f"The video description is : {video.description}")
# print(f"The video views are : {video.views}")
# print(f"The video rating is : {video.rating}")
# print(f"The video duration is : {video.length} s")

# print(video.streams)

# for stream in video.streams:
#     print(stream)

# for stream in video.streams.filter(progressive=True):
#     print(stream)

# for stream in video.streams.filter(progressive=True, res="720p"):
#     print(stream)

# print(video.streams.get_highest_resolution())
# print(video.streams.get_lowest_resolution())

def finish():
    print("Download done")

try:
    if answer == "v":
        lvideo = YouTube(link)
        path = input("Now enter your path : ")
        fname = input("Enter you name : ")
        lvideo.streams.get_highest_resolution().download(output_path=path, filename=fname)
        lvideo.register_on_complete_callback(finish())
    elif answer == "p":
        pvideo = Playlist(link)
        path = input("Enter your path : ")
        for video in pvideo.videos:
            video.streams.get_highest_resolution().download(output_path=path)
        pvideo.register_on_complete_callback(finish())
except:
    print("\nPlease check your link and your download type and try again ...!")
