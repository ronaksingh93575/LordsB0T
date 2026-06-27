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
from utils.drag_screen import right,left
from tasks.go_home import verify_home
from vision.image_finder import find_image
from tasks.back import execute

def run():
    time.sleep(2)

    #verify home screen
    verify_home()
    time.sleep(1)
    pyautogui.click(281,120)
    time.sleep(1)


    def find_login():
        for i in range (1,2):
            daily_login = find_image(f"images/login_reward_{i}.png")
            if daily_login:
                return daily_login
        return None    
        
    pattern = [right,right,right]
    daily_login = find_login()
    for move in pattern:
        if daily_login:
            break
        move()
        time.sleep(1)
        daily_login = find_login()

    if daily_login:
        pyautogui.click(daily_login)
        time.sleep(1)

        claim_login = find_image("images/login_reward_claim.png")

        if claim_login:
            time.sleep(1)
            pyautogui.click(claim_login)

            Logger.log("Daily Login Reward Colelcted")

            time.sleep(1)
            execute()
            time.sleep(1)
            execute()


        else:
            execute()
            left, left,left,left
    else: execute()




run()