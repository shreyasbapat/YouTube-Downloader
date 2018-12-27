import os

import requests

import tkinter as tk
from tkinter import *

from pytube import YouTube

import pyperclip as pc

import validators as vd

from PIL import ImageTk, Image

from io import BytesIO

root = tk.Tk()
root.title("Youtube Video Downloader")
img = ImageTk.PhotoImage(Image.open("Assets/Images/Default.png"))
L_image = Label(root, image=img)


def ret_copied_url():
    url = pc.paste()
    if vd.url(url):
        return url
    else:
        return "https://www.youtube.com/watch?v=32HANv-bdJs"


def callbackInput(v_url):
    print("Changed input.")
    return True


def callbackEntry(v_url):
    return True


def changed(*options):
    print("Changed option: " + selectedOption.get())


# variables
qualityOptions = ["Select Quality"]
selectedOption = StringVar(root)
v_url = StringVar(root)
my_proxy = {"http": "", "https": ""}

v_url.trace("w", lambda name, index, mode, v_url=v_url: callbackInput(v_url))
selectedOption.trace("w", changed)

# Entries
E_url = Entry(
    root,
    textvariable=v_url,
    validate="focusout",
    validatecommand=callbackEntry(v_url),
    width="75",
)
E_url.insert(END, ret_copied_url())

# Menu
qualityOptionsMenu = OptionMenu(root, selectedOption, *qualityOptions)
selectedOption.set("Select Quality")

videoTitle = Label(text="Video title")


def printtit(obj):
    videoTitle.config(text=obj.title)


def onok():
    url = E_url.get()
    print(url)
    video = YouTube(url)
    printtit(obj=video)

    # video.set_filename("DownLoaded YouTube Video")
    videoStreams = video.streams.all()
    qualityOptions = []
    for stream in videoStreams:
        if stream.resolution != None:
            qualityOptions.append(
                stream.resolution + " " + stream.subtype + " tag: " + stream.itag
            )

    # Reset selectedOption and delete all old options
    selectedOption.set("")
    qualityOptionsMenu["menu"].delete(0, "end")

    for option in qualityOptions:
        qualityOptionsMenu["menu"].add_command(
            label=option, command=tk._setit(selectedOption, option)
        )
    selectedOption.set(qualityOptions[0])

    # printing Video Thumbnail
    t_url = video.thumbnail_url
    response = requests.get(t_url)
    img = Image.open(BytesIO(response.content))
    img = ImageTk.PhotoImage(img)
    L_image = Label(root, image=img)
    L_image.place(x=300, y=75, height=90, width=120)
    root.mainloop()


def ondown():
    pathe = os.path.expanduser("~") + "/Downloads"
    os.chdir(pathe)
    url = E_url.get()
    video = YouTube(url)
    selectedOptionList = selectedOption.get().split()

    if not selectedOptionList:
        video.streams.first().download()
        print("Default video downloaded.")
    else:
        selectedItag = selectedOptionList[-1]
        selectedStream = video.streams.get_by_itag(selectedItag)
        selectedStream.download()
        print("Selected video downloaded.")


def Set_proxy_window():
    W_proxy = tk.Toplevel()
    W_proxy.title("Proxy Set-up")
    # variables
    v_http = StringVar(W_proxy)
    v_https = StringVar(W_proxy)
    # Entries
    E_http = Entry(W_proxy, textvariable=v_http)
    E_https = Entry(W_proxy, textvariable=v_https)

    def Set_Proxy():
        print("Setting Proxy")
        if E_http.get() != "" and E_https.get() != "":
            my_proxy["http"] = "http://" + E_http.get()
            my_proxy["https"] = "https://" + E_https.get()
            os.environ["NO_PROXY"] = ""
            print(my_proxy["https"])
        elif E_http.get() != "":
            my_proxy["http"] = "http://" + E_http.get()
            os.environ["NO_PROXY"] = "https://*"
        elif E_https.get() != "":
            my_proxy["https"] = "https://" + E_https.get()
            os.environ["NO_PROXY"] = "http://*"
        else:
            os.environ["NO_PROXY"] = "*"
        os.environ["HTTP_PROXY"] = my_proxy["http"]
        os.environ["HTTPS_PROXY"] = my_proxy["https"]
        W_proxy.destroy()

    # Buttons
    B_okay = Button(W_proxy, text="Okay", command=Set_Proxy)
    B_cancel = Button(W_proxy, text="Cancel", command=W_proxy.destroy)
    # Placing
    Label(W_proxy, text="http :").place(x=15, y=15)
    E_http.place(x=65, y=15)
    Label(W_proxy, text="https :").place(x=15, y=40)
    E_https.place(x=65, y=40)
    B_okay.place(x=20, y=70)
    B_cancel.place(x=155, y=70)
    # setting proxy window size and position
    W_proxy.geometry("250x110+300+300")


def func(event):
    pathe = os.path.expanduser("~") + "/Downloads"
    os.chdir(pathe)
    url = E_url.get()
    video = YouTube(url)
    stream = video.streams.first()
    print(os.getcwd())
    stream.download()


root.bind("<Return>", func)

# Buttons
B_refresh = Button(root, text="Refresh", command=onok)
B_setproxy = Button(root, text="Set Proxy", command=Set_proxy_window)
B_downlaod = Button(root, text="Download", command=ondown)
B_exit = Button(root, text="CLOSE", fg="red", command=root.destroy)

# Placing
Label(text="Link :").place(x=20, y=20)
E_url.place(y=20, x=60, width=400)
videoTitle.place(x=25, y=50, width=450)
qualityOptionsMenu.place(x=25, y=75, width=180)
B_setproxy.place(x=25, y=110)
B_downlaod.place(x=115, y=110)
B_exit.place(x=80, y=145)
B_refresh.place(y=170, x=320)
L_image.place(x=300, y=75, height=90, width=120)

# setting root window size and position
root.geometry("475x205+300+300")
root.mainloop()
