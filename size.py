import os
from PIL import Image

path = "/media/Documents/Python/scripts/wallpapers/"
width = 1920
height = 1080

def getFiles():
    files = os.listdir(path)
    # Sort by creation date
    files.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    return files

def deleteFiles():
    files = getFiles()
    print("DELETING started.") 
    for file in files:
        try:
            im = Image.open(path+file)
            if im.size[0] != width or im.size[1] != height:
                os.remove(path + '/' + file)
                print("DELETED " + file + " (" + im.size[0] + ", " + im.size[1] + ")")
            im.close()
        except OSError:
            os.remove(path + '/' + file)
            print("DELETED CORRUPTED " + file)
    print("DELETING completed.") 

if __name__ == "__main__":
    deleteFiles()
