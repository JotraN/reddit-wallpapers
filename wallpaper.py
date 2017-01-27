import sys
import praw
import time
import os
from urllib.request import urlretrieve
from PIL import Image
import config

def get_files(path):
    files = os.listdir(path)
    # Sort by creation date
    files.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    return files

def delete_old_files(path):
    files = get_files(path)
    numOfFiles = len(files)
    i = 0
    while numOfFiles > config.max_num_of_wallpapers:
        os.remove(path + '/' + files[i])
        i += 1
        numOfFiles -= 1

def download_wallpapers(reddit, path, subreddit, downloaded_files):
    sub = reddit.subreddit(subreddit)
    for post in sub.top(limit=config.max_num_of_posts):
        # Download new wallpapers and rename it using its size
        if post.url not in downloaded_files:
            if not (str(post.url).endswith(".png") or str(post.url).endswith(".jpg") 
                    or str(post.url).endswith(".jpeg")):
                post.url = post.url + ".png"
            downloaded_files.append(post.url)
            tmpfile = path + '/' + str(hash(post.url))
            try:
                urlretrieve(post.url, tmpfile)
                # Don't save any failed/incomplete downloads
                if os.path.getsize(tmpfile) > 100000:
                    os.rename(tmpfile, path + '/' + str(os.path.getsize(tmpfile)) 
                            + ".png")
                else:
                    os.remove(tmpfile);
            except Exception as e:
                pass
    delete_old_files(path)

def change_wallpaper(path, system_command):
    files = get_files(path)
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
    os.system(system_command)
    print("Wallpaper changed.")

def delete_wrong_size_wallpapers(path, width, height):
    print("DELETING started.") 
    files = get_files(path)
    for file in files:
        try:
            im = Image.open(path+file)
            # Only keep wallpapers that are at least the min width and height.
            if im.size[0] < width or im.size[1] < height:
                os.remove(path + '/' + file)
                print("DELETED " + file + " (" + str(im.size[0]) + ", " + str(im.size[1]) + ")")
            im.close()
        except OSError:
            os.remove(path + '/' + file)
            print("DELETED CORRUPTED " + file)
    print("DELETING completed.") 

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "reload":
        change_wallpaper(config.wallpapers_path, config.system_command)
        return
    downloaded_files = []
    # Wait a minute before starting to ensure an internet connection
    time.sleep(60)
    while True:
        wallpapers_path = config.wallpapers_path
        userAgent = ("Wallpaper Downloader")
        r = praw.Reddit(user_agent=userAgent,
                client_id=config.client_id, 
                client_secret=config.client_secret)
        download_wallpapers(r, wallpapers_path, config.subreddit, downloaded_files)
        if config.size_matters:
            delete_wrong_size_wallpapers(wallpapers_path, config.width, 
                    config.height)
        change_wallpaper(wallpapers_path, config.system_command)
        time.sleep(config.change_time)

if __name__ == "__main__":
    main()
