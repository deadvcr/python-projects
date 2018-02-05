#######################################
# Minecraft Server Map Update Script  #
#      "It does it goodly"            #
#######################################

import shutil
import datetime
import os
import time as jeff


worldList = [
    "/mnt/data/servers/minecraft/world",
    "/mnt/data/servers/minecraft/pixelartworld",
    "/mnt/data/servers/minecraft/survival",
    "/mnt/data/servers/minecraft/world_nether",
    "/mnt/data/servers/minecraft/world_the_end"
]

worldName = [
    "mainworld",
    "pixelartworld",
    "survivalworld",
    "nether",
    "end"
]

def mapUpdate(folders, worldName):
    for index, name in enumerate(folders):
        filename = worldName[index] + "-" + date

        shutil.make_archive(filename, 'zip', name)
        if not os.path.exists('/var/www/html/maps/' + date + '/'):
            os.mkdir('/var/www/html/maps/' + date + "/")
        shutil.move(filename + ".zip", "/var/www/html/maps/" + date + "/" + filename + ".zip")

def getTime():
    time = datetime.datetime.now()
    date = time.isoformat()
    return date


while True:
    date = getTime()
    mapUpdate(worldList, worldName)
    print("Complete! Next update in 6 hours.")
    jeff.sleep(21600)
