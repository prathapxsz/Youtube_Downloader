from pytube import YouTube

url = input("Enter the url: ")
yt = YouTube(url)
#streams = []
streams = yt.streams.filter(progressive = True).all()
print(streams)
itag = input("Enter itag youo wish to download: ")
yt.streams.get_by_itag(itag).download(output_path='/myTools/github/Youtube_downloader/downloads/')
print("Video Downloaded")
