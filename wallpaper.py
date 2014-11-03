import sys
import praw
import time
import os
from urllib.request import urlretrieve
import size

path = "/media/Documents/Python/scripts/wallpapers/"
maxAmt = 500
postAmt = 15
waitTime = 1800
subreddit = "wallpaper+wallpapers+spaceporn"
wallpaperCmd = "exec feh --bg-center '" + path + "wallpaper.png'"
sizeMatters = True

def getFiles():
    files = os.listdir(path)
    # Sort by creation date
    files.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    return files

def delete():
    files = getFiles()
    size = len(files)
    i = 0
    while size > maxAmt:
        os.remove(path + '/' + files[i])
        i += 1
        size -= 1

def download(downloadedFiles):
    userAgent = ("Wallpaper Downloader")
    r = praw.Reddit(user_agent=userAgent)
    sub = r.get_subreddit(subreddit)
    for post in sub.get_top(limit=postAmt):
        # Download new wallpapers and rename it using its size
        if post.url not in downloadedFiles:
            if not (str(post.url).endswith(".png") or str(post.url).endswith(".jpg") or str(post.url).endswith(".jpeg")):
                post.url = post.url + ".png"
            downloadedFiles.append(post.url)
            tmpfile = path + '/' + str(hash(post.url))
            try:
                urlretrieve(post.url, tmpfile)
                # Don't save any failed/incomplete downloads
                if os.path.getsize(tmpfile) > 100000:
                    os.rename(tmpfile, path + '/' + str(os.path.getsize(tmpfile)) + ".png")
                else:
                    os.remove(tmpfile);
            except Exception as e:
                pass
    # Delete oldest wallpapers after reaching maxAmt.
    delete()

def change():
    files = getFiles()
    wallNum = 0
    # Rename previous wallpaper
    for i in range(len(files)):
        if "wallpaper" in files[i]:
            wallNum = i+1
            if i == len(files)-1:
                wallNum = 0
            fullpath = path + files[i]
            os.rename(fullpath, path + str(os.path.getsize(fullpath)) + ".png")
            break
    # Name new wallpaper
    if "wallpaper" not in files[wallNum]:
        fullpath = path + files[wallNum]   
        os.rename(fullpath, path + "wallpaper.png")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "reload":
        change()
        os.system(wallpaperCmd)
        return
    downloadedFiles = []
    # Wait a minute before starting to ensure an internet connection
    time.sleep(60)
    while True:
        download(downloadedFiles)
        change()
        os.system(wallpaperCmd)
        if sizeMatters:
            size.deleteFiles();
        time.sleep(waitTime)

if __name__ == "__main__":
    main()
