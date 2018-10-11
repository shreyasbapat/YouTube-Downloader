import os
import tkinter
from tkinter import *
from pytube import YouTube

root = Tk()
root.title('YouTube Video Downloader')
Label(text='Put the link here in the box below: ').pack(side=TOP,padx=10,pady=10)

entry = Entry(root, width=50)
entry.pack(side=TOP,padx=10,pady=10)
file_path = os.path.dirname(os.path.realpath(__file__))

def printtit(obj):
	Label(text=obj.title).pack(side=BOTTOM,padx=10,pady=10)

def onok():
    url = entry.get()
    video = YouTube(url)
    printtit(obj=video)
#     video.set_filename("DownLoaded YouTube Video")

def ondown():
    pathe = os.path.expanduser('~') + "/Downloads"
    os.chdir(pathe)
    url = entry.get()
    video = YouTube(url)
    stream = video.streams.first()
    print(os.getcwd())
    stream.download()

def desk():
    print(file_path)
    entry = "[Desktop Entry] \nName=YouTube Downloader \nVersion=1.0 \n" \
            "Exec=file_path + "/YouTube \n" \
            "Icon=/usr/share/pixmaps/python.xpm \nComment=Download YT videos \n" \
            "Type=Application \nTerminal=false \nStartupNotify=true \n" \
            "Categories=Video;GTK;GNOME"
    entrypath = os.path.expanduser('~') + "/.local/share/applications/"
    os.chdir(entrypath)
    f = open("YouTube.desktop" , "w")
    f.write("%s" % entry)
    f.close()

def func(event):
    pathe = os.path.expanduser('~') + "/Downloads"
    os.chdir(pathe)
    url = entry.get()
    video = YouTube(url)
    stream = video.streams.first()
    print(os.getcwd())
    stream.download()

root.bind('<Return>', func)
Button(root, text='View', command=onok).pack(side=TOP)
Button(root, text='Download', command=ondown).pack(side=LEFT)
Button(root, text='CLOSE',fg="red",command=root.destroy).pack(side= RIGHT)
Button(root, text='DesktopEntry', command=desk).pack(side=BOTTOM)

root.mainloop()
