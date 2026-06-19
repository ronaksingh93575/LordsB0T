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
import re
from database.supabase_db import update_shield_status
from tasks.back import execute
from logs.logger import Logger
from vision.image_finder import find_image
from vision.screenshot import capture_region
from vision.ocr import read_image

def run(username):
# Pause for for 2 sec
    time.sleep(1)

    # Define your target coordinates
    target_x = 991
    target_y = 251
    Logger.log("Switching to truf boost")
    # Move to the coordinates and perform a standard left click
    pyautogui.click(x=target_x, y=target_y)

    Logger.log("Checking Shield")
    time.sleep(1)

    image = capture_region(
        566,
        302,
        150,
        60,
    )

    image = read_image(image)
    Logger.log(image)
    shield_time = None

    # for text in image:
    #     if re.match(r"\d{2}\.d{2}\.d{2}",text):
    #         shield_time = text
    #         break

    # import re

    #----------------------------
    # Time into seconds logic
    #----------------------------

    def shield_to_seconds(text):
        try:

            text = text.replace(".", ":")

            days = 0

            day_match = re.search(
                r"(\d+)d",
                text.lower()
            )

            if day_match:

                days = int(
                    day_match.group(1)
                )

                text = re.sub(
                    r"\d+d",
                    "",
                    text.lower()
                ).strip()

            hours, minutes, seconds = map(
                int,
                text.split(":")
            )

            total_seconds = (
                days * 86400
                + hours * 3600
                + minutes * 60
                + seconds
            )

            return total_seconds
        except Exception:
            return 0

    minimum_time = 8
    desired_second = (minimum_time*3600)
    time.sleep(1)

    if image :
        current_time = shield_to_seconds(image[0])

        Logger.log(f"Time left : {current_time} seconds")

        if current_time >= desired_second:
            update_shield_status(
                username,
                True,
                image[0],
                current_time
            )
            execute()
        else:
            # location = find_image("images/shield.png"
            # )
            # location = find_image("images/shield.png")
            Logger.log("Updating Shield")
            time.sleep(1)

            #truf defence opened

            target_x = 470
            target_y = 321
            pyautogui.click(x=target_x, y = target_y)
            time.sleep(1)

            #applying shield

            target_x = 763
            target_y = 306
            pyautogui.click(x=target_x, y=target_y)

            #------------------------
            # if notice appears
            #------------------------

            notice = capture_region(
                    358,
                    167,
                    50,
                    50,
                )
            notice = read_image(notice)
            if notice:
                target_x = 582
                target_y = 287
                pyautogui.click(x=target_x, y = target_y)
            else:
                pass

            Logger.log("Shield Updated")
            time.sleep(1)

            #------------------------
            # new shield stats
            #------------------------

            image = capture_region(
                    566,
                    302,
                    150,
                    60,
                )

            image = read_image(image)
            time.sleep(2)
            Logger.log(image)

            current_time = shield_to_seconds(
                image[0]
            )
            update_shield_status(
                username,
                1,
                image[0],
                current_time
            )

            #back to home screen

            execute()



    else: pass






