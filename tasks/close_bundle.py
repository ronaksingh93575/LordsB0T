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
from tasks.back import execute
from logs.logger import Logger
from vision.image_finder import find_image
from vision.clicker import click


def run():

    Logger.log(
        "Searching popup..."
    )
    execute()
    time.sleep(1)
    execute()

    while True:

        location = find_close()

        if not location:
            break

        pyautogui.click(location)

        Logger.log(
            "Bundle popup closed."
        )

        time.sleep(1)

    Logger.log(
        "Bundle popup not found."
        )


def find_close():
    for i in range(1,8):
        location = find_image(
            f"images/close_{i}.png"
        )

        if location:
            return location
    
    return None