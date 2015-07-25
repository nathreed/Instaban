import serial
import time
import subprocess
#Some important things
serverFolderPath = "/path/to/minecraft/server/folder"
exemptPlayers = ["list", "of", "exempt", "players", "goes", "here"]
#Define some functions we may want to use
def serverCommand(command):
	#print "Sending server command: ", command
	pathToDirectCommand = serverFolderPath + "/scripts/direct_command.sh" 
	subprocess.Popen(["bash", pathToDirectCommand, command])

#This is not my code, got it from http://stackoverflow.com/a/7047765
def tail(f, window=20):
    """
    Returns the last `window` lines of file `f` as a list.
    """
    if window == 0:
        return []
    BUFSIZ = 1024
    f.seek(0, 2)
    bytes = f.tell()
    size = window + 1
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if bytes - BUFSIZ > 0:
            # Seek back one whole BUFSIZ
            f.seek(block * BUFSIZ, 2)
            # read BUFFER
            data.insert(0, f.read(BUFSIZ))
        else:
            # file too small, start from begining
            f.seek(0,0)
            # only read what was not read
            data.insert(0, f.read(bytes))
        linesFound = data[0].count('\n')
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
    return ''.join(data).splitlines()[-window:]
#End the part that's not my code

#ttyACM0 is the serial port for the arduino connection. Edit to fit proper serial port on your system.
serialController = serial.Serial("/dev/ttyACM0", 9600)
serverLog = open(serverFolderPath + "/logs/latest.log", "r")
serverLog.seek(0,2)
while True:
	#The main loop of our little python program
	
	serialController.flushInput()
  '''
	This variable assignment will not finish until the button is
	pressed. Then we do stuff to the server.
	'''
	serialLine = serialController.readline() 
	#Do stuff to MC server here
	#You can print whatever you want here or nothing at all
	print "Whipped out my can of insta-ban"
	#We don't care about the rest of the stuff until the next time through and we dont want stuff messing with our list command
	serverLog.flush()
	#First tell the server to list its players
	serverCommand("list")
	time.sleep(0.1)
	#And get the server's response from its log
	#This is really nasty code and could probably be condensed into fewer steps
	#I just wanted to get it working
	playerListLine = tail(serverLog, 1)
	playerListLineArray = playerListLine[0].split(":")
	playerListStrings = playerListLineArray[3]
	playersArrayPreStrip = playerListStrings.split(",")
	playersArray = []
	for player in playersArrayPreStrip:
		playersArray.append(player.lstrip())
	
	#Finally iterate through the players and ban everyone except the exempt players
	for player in playersArray:
		if not player in exemptPlayers:
			serverCommand("ban " + player)
	#To prevent spamming the button and screwing things up, wait for 1 second before checking if the button is pressed again
	time.sleep(1)
