#from pytube import YouTube

#link = 'https://www.youtube.com/watch?v=QEbBuW8u1bA'
#link = input("Please enter the video url: ")

#video = YouTube(link)

#print(f"The video title is:\n{video.title} \n--------------------------------")
#print(f"The video description is:\n{video.description} \n--------------------------------")
#print(f"The video views are:\n{video.views} \n--------------------------------")
#print(f"The video rating is:\n{video.rating} \n--------------------------------")
#print(f"The video duration is:\n{video.length/60} minutes \n--------------------------------")

#print(video.streams)

#for stream in video.streams:
    #print(stream)

#for stream in video.streams.filter(progressive=True):
    #print(stream)

#for stream in video.streams.filter(res="720p"):
    #print(stream)

#for stream in video.streams.filter(subtype='mp4'):
    #print(stream)

#for stream in video.streams.filter(res='1080p'):
    #print(stream)

#print(video.streams.get_highest_resolution())
#print(video.streams.get_lowest_resolution())

def finish():
    print("Download Done")

#video.streams.get_lowest_resolution().download(output_path="C:/Users/PC/Desktop/python_projects")
#video.register_on_complete_callback(finish())

from pytube import Playlist


p = Playlist('https://www.youtube.com/playlist?list=PLvH62d_YT64wsYx6LtLnm5BhThJMYLrsg')

for video in p.videos:
    video.streams.first().download(output_path="C:/Users/PC/Desktop/python_projects")
    video.register_on_complete_callback(finish())
    
