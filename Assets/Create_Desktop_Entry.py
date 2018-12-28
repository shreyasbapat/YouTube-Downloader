import shutil
import os
import pwd

# .desktop file
source = "/home/" + pwd.getpwuid(os.getuid())[0] + "/YouTube-Downloader"
dest1 = "/home/" + pwd.getpwuid(os.getuid())[0] + "/.local/share/applications"

shutil.move(source + "/YouTube_Downloader.desktop", dest1)

# exec file
source = "/home/" + pwd.getpwuid(os.getuid())[0] + "/YouTube-Downloader"
dest1 = "/home/" + pwd.getpwuid(os.getuid())[0] + "/usr/share"

shutil.move(source + "/ytd", dest1)

# .desktop file
source = "/home/" + pwd.getpwuid(os.getuid())[0] + "/YouTube-Downloader"
dest1 = "/home/" + pwd.getpwuid(os.getuid())[0] + "/usr/share/pixmaps"

shutil.move(source + "/ytd.png", dest1)
