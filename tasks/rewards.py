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
from vision.image_finder import find_image

def run(username):

    for i in range(1,3):

        guild = find_image(f"images/guild_{i}.png")

        if guild:
            return guild
        
    time.sleep(1)
    pyautogui.click(guild)


        