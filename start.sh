screen -dmS MinecraftServer
screen -p 0 -S MinecraftServer -X eval 'stuff "java -Xmx2G -jar minecraft_server*.jar"\015'
