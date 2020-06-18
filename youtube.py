# import module
from pytube import YouTube

video = YouTube('https://www.youtube.com/watch?v=dsY9sncnRLc') # youtube video link
filtered = video.streams.filter(file_extension = "mp4").all()[0] #mp4 videos. I am selecting the first result.

filtered_str = str(filtered)

'''
print(filtered_str)

<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">

'''

# next few lines to get itag from the string 
params = filtered_str.split(" ")

itag = 0
for param in params:
	if "itag" in param:
		itag = param.split("=")[1]

itag = itag.strip('"')
itag = int(itag)

# You can pass path, by default it saves in the cwd
video.streams.get_by_itag(itag).download()