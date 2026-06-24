import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import time
import pyautogui
from logs.logger import Logger
from ui import settings
from vision.image_finder import find_image


def run(username):
    #pause for 2 sec
    Logger.log("confirming Home Screen")
    time.sleep(1)   
    
    #----------------------------------
    # cehcking if we are at home or not
    #----------------------------------
    location = find_image("images/kingdom_map_1")
    Logger.log("Attempt 1")

    if not location:
        location = find_image("images/kingdom_map_2")

    elif not location:
        location = find_image("images/kingdom_map_3")

    elif not location:
        location = find_image("images/kingdom_map_4")

    if location:
        Logger.log(f"Home Kingdom Verified :{location}")

    else:
        pass