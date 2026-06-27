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
import random
from tasks.back import execute
from logs.logger import Logger
from vision.image_finder import find_image
from utils.drag_screen import forward, backward

def run():
    time.sleep(1)
    def find_cargo_chip():

        for i in range(1,2):
            cargo_ship = find_image(f"images/cargo_ship_{i}.png")
            if cargo_ship:
                return cargo_ship
        return None

    pattern = random.choice([forward(), backward()])

    for move in pattern:
        move()
        time.sleep(2)
        cargo_ship = find_cargo_chip()
        if cargo_ship:
            break
    if cargo_ship:
        Logger.log("Cargo Ship Found")
        pyautogui.click(cargo_ship)
        time.sleep(1)

        check_ship = find_image("images/cargo_ship_exchanged.png")
        if not check_ship:

            pyautogui.click(282, 379)
            use_rss = find_image("images/use_rss.png")
            if use_rss:
                pyautogui.click(use_rss)
                Logger.log("Trade Succesfull")

            time.sleep(1)
            pyautogui.click(740, 379)
            if use_rss:
                pyautogui.click(use_rss)
                Logger.log("Trade Succesfull")

            time.sleep(1)
            pyautogui.click(282, 547)
            if use_rss:
                pyautogui.click(use_rss)
                Logger.log("Trade Succesfull")

            time.sleep(1)
            pyautogui.click(740, 547)
            if use_rss:
                pyautogui.click(use_rss)
                Logger.log("Trade Succesfull")
            execute()
        execute()

    else:
        Logger.log("Cargo Ship Not Found")




        


