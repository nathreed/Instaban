# Instaban
The python code and shell scripts for my Can of Insta-Ban project. Licensed under the MIT License. See LICENSE file for complete text.  

##Project description  
The Can of Insta-Ban is a repurposed shaving cream can with an Arduino inside. The arduino is running a very basic sketch that just writes output to serial whenever a button is pressed. The real work is done in the python script, `serialMonitor.py`.  
Images at http://imgur.com/a/KI9Lh.  
WARNING: The code here is really nasty in some places and lots of it (like `direct_command.sh`) is completely unnecessary and could be incorporated into the main file. I just wanted to get the code working so it's not all that pretty. It does work though.


## What all the files do  
### `start.sh`  
This starts the Minecraft server in a GNU screen session. You would use this in place of your regular start script.  
### `cleanup.sh`  
This kills the screen session. You can run it after you have stopped the MC server from the GUI.  
### `serialMonitor.py`  
This is the main python script for the project. It receives messages from the Arduino over serial and bans players on the minecraft server when that happens. The Arduino is not actually sending anything meaningful over the serial connection, it's really just the fact that it's sending something when the button is pressed that this script relies on.
### `direct_command.sh`  
This is a somewhat unnecessary script (its functionality could be integrated into `serialMonitor.py` with `subprocess` but I was spending too much time trying to figure out escaping quotes in the command). This pretty much accepts a command to send to the server as its only argument and then sends it to the server's screen session.  
