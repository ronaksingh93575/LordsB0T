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
from vision.ocr import read_image
from vision.screenshot import capture_region
from utils.drag_screen import up, down


def run():
    time.sleep(1)
    familiar_skills = find_image("images/familar_skills.png")
    if familiar_skills:
        pyautogui.click(familiar_skills)
        time.sleep(1)

        for _ in range(10):
            for i in range(1,3):
                use = find_image(f"images/familiar_skill_use_{i}.png")
                if use:
                    break
            if use:
                #x, y of use button
                x,y = use

                #capturing the area to know skill name
                skill_name = capture_region(
                    x - 621,
                    y - 50,
                    220,
                    40
                )
                skill_name = read_image(skill_name)
                
                Logger.log(f"Skill Used : {''.join(skill_name)}")
                pyautogui.click(use)
                time.sleep(2)
            down()
            time.sleep(1)

        for _ in range(10):
            up()
            time.sleep(1)
        execute()

    else:
        Logger.log("Not Found")    

run()