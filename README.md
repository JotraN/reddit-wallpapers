# Reddit Wallpapers
Small script that retrieves and sets wallpapers from Reddit.

# Installation
Python (3.6.0) is required to run the script, as well as the libraries 
defined in the "Libraries Required" section.

User specific configuration options can be found in the <code>config.py</code> file.<br>
It is important to supply your own Reddit client id and secret - these are necessary 
for the script to interact with Reddit.

Run this script just as you would any python script.

<h1>Tips</h1>
Run this script at start-up.<br>
Running with the <em>reload</em> flag will change the current wallpaper manually.<br>
If you're using this on Windows, you can set <code>system_command</code> to an empty 
string ("") and just point Windows to the directory.<br>

## Libraries Required
<a href="https://praw.readthedocs.org/">PRAW (4.3.0)</a><br>
<a href="https://pillow.readthedocs.org/">Pillow (4.0.0)</a><br>

## License
This project is licensed under the terms of the MIT license.
