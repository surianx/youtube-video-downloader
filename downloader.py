from pytubefix import YouTube

link = input("put a link here: ")
yt = YouTube(link)

downloadingthing = yt.streams.get_highest_resolution()
print("downloading")

downloadingthing.download(filename="urvideo.mp4")
print("donedownloading")
