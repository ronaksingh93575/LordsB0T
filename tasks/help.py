import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import pyautogui
from logs.logger import Logger
from vision.image_finder import find_image

def run():
    while True:
        press_help = find_image("images/help.png")

        if not press_help:
            break

        if press_help:
            pyautogui.click(press_help)
            Logger.log("Guild help pressed")

    return True
