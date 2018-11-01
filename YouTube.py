import os
import tkinter as tk
from tkinter import *
from pytube import YouTube

root = tk.Tk()
root.title('YouTube Video Downloader')
Label(text='Put the link here in the box below: ').pack(side=TOP,padx=10,pady=10)

qualityOptions = ['Click View options button']
selectedOption = StringVar(root)
# selectedOption.set('')

def callbackInput(sv):
    print("Changed input.")
    return True

def callbackEntry(sv):
    return True

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callbackInput(sv))
entry = Entry(root, textvariable=sv, validate='focusout', validatecommand=callbackEntry(sv), width='75')
entry.insert(END, 'https://www.youtube.com/watch?v=32HANv-bdJs')
entry.pack(side=TOP,padx=10,pady=10)

videoTitle = Label(text='Video title')
videoTitle.pack(side=BOTTOM, padx=10, pady=10)

# Show video title
def printtit(obj):
	videoTitle.config(text = obj.title)

def onok():
    url = entry.get()
    video = YouTube(url)

    printtit(obj=video)

    # video.set_filename("DownLoaded YouTube Video")
    videoStreams = video.streams.all()
    qualityOptions = []
    for stream in videoStreams:
        if stream.resolution != None:
            qualityOptions.append(stream.resolution + ' ' + stream.subtype + ' tag: ' + stream.itag)

    # Reset selectedOption and delete all old options
    selectedOption.set('')
    qualityOptionsMenu['menu'].delete(0, 'end')

    for option in qualityOptions:
        qualityOptionsMenu['menu'].add_command(label=option, command=tk._setit(selectedOption, option))
    selectedOption.set(qualityOptions[0])


def ondown():
    pathe = os.path.expanduser('~') + "/Downloads"
    os.chdir(pathe)
    url = entry.get()
    video = YouTube(url)
    selectedOptionList = selectedOption.get().split()
    
    if not selectedOptionList:
        video.streams.first().download()
        print('Default video downloaded.')
    else:
        selectedItag = selectedOptionList[-1]
        selectedStream = video.streams.get_by_itag(selectedItag)
        selectedStream.download()
        print('Selected video downloaded.')

def func(event):
    pathe = os.path.expanduser('~') + "/Downloads"
    os.chdir(pathe)
    url = entry.get()
    video = YouTube(url)
    stream = video.streams.first()
    print(os.getcwd())
    stream.download()

root.bind('<Return>', func)

# Video Options
qualityOptionsMenu = OptionMenu(root, selectedOption, *qualityOptions)
qualityOptionsMenu.pack()

def changed(*options):
    print('Changed option: ' + selectedOption.get())

selectedOption.trace('w', changed)

Button(root, text='View options', command=onok).pack(side=TOP)
Button(root, text='Download', command=ondown).pack(side=LEFT)
Button(root, text='CLOSE',fg="red",command=root.destroy).pack(side= RIGHT)

root.mainloop()
