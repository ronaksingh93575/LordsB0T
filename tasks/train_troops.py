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
from utils.drag_screen import right, left, up, down


def run():
    #pause for 2 sec
    Logger.log("confirming Home Screen")
    time.sleep(1)   
    
    #----------------------------------
    # cehcking if we are at home or not
    #----------------------------------
    def verify_home():

        location_map = find_image("images/kingdom_map_1.png")

        if not location_map:
            location_map = find_image("images/kingdom_map_2.png")

        if not location_map:
            location_map = find_image("images/kingdom_map_3.png")

        if not location_map:
            location_map = find_image("images/kingdom_map_4.png")
            
        return location_map

    location_map = verify_home()

    if not location_map:
        pyautogui.click(x=69, y=528)

        time.sleep(2)

        location_map = verify_home()
    Logger.log("Truf verified")
    #----------------------------------
    # searching for barracks
    #----------------------------------

    Logger.log("Looking for Barracks")
    time.sleep(2)

    def find_barracks():
        location_barracks = find_image(
            "images/barracks_lv25.png"
        )
        if not location_barracks:
            location_barracks = find_image(
                "images/barracks_lv15.png"
            )
        return location_barracks

    search_moves = [
        right,
        lambda: left(2),
        left,
        down
    ]

    location_barracks = find_barracks()

    for move in search_moves:

        if location_barracks:
            break

        move()
        time.sleep(1)

        location_barracks = find_barracks()
    
    if location_barracks:
        Logger.log("Barracks Found")

        pyautogui.click(location_barracks)

        Logger.log("Barracks opened")
        return
run()