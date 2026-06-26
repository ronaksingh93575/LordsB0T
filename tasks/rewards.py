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
from tasks.back import execute
from vision.image_finder import find_image

def run(username):

    time.sleep(2)

    for i in range(1,6):
        guild = find_image(f"images/guild_{i}.png")
        if guild:
                break
        
    if guild:
        time.sleep(1)
        pyautogui.click(guild)

        guild_board = find_image("images/guild_board.png")
        time.sleep(2)
        if not guild_board:
            pyautogui.click(944, 190)
            time.sleep(2)

         
    loots = None

    for i in range(0,5):
        loots = find_image(f"images/loot_{i}.png")
        if loots:
            break
        
    if loots:
        time.sleep(1)
        pyautogui.click(loots)
        time.sleep(2)

        open_loots = find_image("images/open_all_loot.png")
        if open_loots:
            time.sleep(5)
            pyautogui.click(open_loots)
            delete_loots = find_image("images/delete_all_loot.png")
            time.sleep(5)
            pyautogui.click(delete_loots)
        else:
            while True:
                time.sleep(2)
                open_loot = find_image("images/open_loot.png")
                delete_loot = find_image("images/delete_loot.png")

                if open_loot and delete_loot:
                    pyautogui.click(open_loot)
                    time.sleep(1)

                    pyautogui.click(delete_loot)
                    time.sleep(1)

                else:
                    pass
                
        Logger.log("Loot checked")

        time.sleep(5)        
        execute()
        time.sleep(5)
        execute()
        

