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
import time
from vision.image_finder import find_image
from tasks.back import execute

def verify_home():

    for i in range(1,5):
        kingdom_map = find_image(f"images/kingdom_map_{i}.png")

        if kingdom_map:
            return kingdom_map

    if not kingdom_map:
        truf_map = find_image("images/truf_map.png")
        if truf_map:
            pyautogui.click(truf_map)
        
        else:
            execute()

        time.sleep(2)

        kingdom_map = verify_home()
        