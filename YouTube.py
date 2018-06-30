import tkinter
from tkinter import *
from pytube import YouTube

root = Tk()
root.title('YouTube Video Downloader')
Label(text='Put the link here in the box below: ').pack(side=TOP,padx=10,pady=10)

entry = Entry(root, width=50)
entry.pack(side=TOP,padx=10,pady=10)
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

def printtit(obj):
	Label(text=obj.title).pack(side=BOTTOM,padx=10,pady=10)

def onok(link ="https://www.youtube.com/watch?v=xWOoBJUqlbI"):
    url = entry.get()
    video = YouTube(url)
    printtit(obj=video)
#     video.set_filename("DownLoaded YouTube Video")
def ondown(link ="https://www.youtube.com/watch?v=xWOoBJUqlbI"):
    url = entry.get()
    video = YouTube(url)
    stream = video.streams.first()

    stream.download()
    
    
def func(event):
    url = entry.get()
    video = YouTube(url)
    stream = video.streams.first()

    stream.download()

root.bind('<Return>', func)
Button(root, text='View', command=onok).pack(side=TOP)
Button(root, text='Download', command=ondown).pack(side=LEFT)
Button(root, text='CLOSE',fg="red",command=root.destroy).pack(side= RIGHT)

root.mainloop()
