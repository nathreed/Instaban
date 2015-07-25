#!/bin/bash
CMD_STRING=$1

#echo $CMD_STRING > dc.log
screen -p 0 -S MinecraftServer -X eval "stuff '${CMD_STRING}'\015"
