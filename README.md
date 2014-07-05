<h1>Set Up</h1>
<strong>This script uses PRAW (you'll need it installed).</strong><br>
At the beginning of the script, you should find the following right underneath the imports:<br>
<img src="params.png" alt="Params"/><br>
<strong>>path</strong> - the full path to the location to save/keep the wallpapers.<br>
<strong>maxAmt</strong> - the max amount of wallpapers to keep saved.<br>
<strong>postAmt</strong> - the amount of top posts (wallpapers) to save each time the script downloads wallpapers.<br>
<strong>waitTime</strong> - the amount of time in seconds to wait to update wallpapers. Default is 30 mins.<br>
<strong>subreddit</strong> - the subreddit(s) to download from. Seperate multiple subreddits by using a '+'.<br>
<strong>wallpaperCmd</strong> - the system command used to change wallpapers. Default assumes you are using feh to set your wallpaper.<br>
Just change these to however you see fit.<br>

Run this script just as you would any python script, by using the following command:<br>
<em>python wallpaper.py &</em><br>
assuming you are in the directory that contains wallpaper.pu.
The '&' will run it in the background.

<h1>Tips</h1>
Run this script at start-up.<br>
Running <em>python wallpaper.py reload</em> will change the current wallpaper manually.<br>
You should bind this command to allow for even easier changing of wallpapers (I have it binded to SUPER+CTRL+SHIFT+R).<br>
If you're using this on Windows, you can set <strong>wallpaperCmd</strong> to an empty string ("") and just point Windows to the directory.<br>
Sometimes wallpapers still manage to fail to download. You'll have to delete these manually or just let it sit in your directory until the script deletes it due to age.<br>
