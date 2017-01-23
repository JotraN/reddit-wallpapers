import os

### Reddit Options
max_num_of_posts = 15
subreddit = "wallpaper+wallpapers+spaceporn+WidescreenWallpaper+WQHD_Wallpaper"
client_id = os.environ["RED_CLIENT_ID"]
client_secret = os.environ["RED_CLIENT_SECRET"]

### System Options
# Path to download wallpapers to.
wallpapers_path = "/media/Documents/Python/scripts/wallpapers/"
# Max number of wallpapers to keep in the folder.
max_num_of_wallpapers = 500
# Time (in seconds) between downloading/changing wallpapers.
change_time = 1800
# Command used to change wallpapers.
system_command = "exec feh --bg-fill '" + wallpapers_path + "wallpaper.png'"
# Only keep wallpapers with following width and height.
size_matters = True
width = 3440
height = 1440
