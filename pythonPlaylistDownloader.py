# Make sure to install pytube module in this way : C:\> pip install git+https://github.com/baxterisme/pytube

# import pytube
from pytube import YouTube
from pytube import Playlist

link = "https://www.youtube.com/playlist?list=PLQV_Ef4ahCVx8GfaLPcHhDXVamvHLnqsw" #insert the playlist link here

video_links = Playlist(link)
#print()
for video in video_links:
	#print(video)
	yt = YouTube(video)
	stream = yt.streams.filter(progressive= True, file_extension = 'mp4').order_by('resolution').first() #Quality of video can be changes from here, also ordering by resolution, sorts it in increasing quality and first() selects 360p here
	stream.download()
	print("Downloaded: " + yt.title)