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
import re
from logs.logger import Logger
from ui import settings
from tasks.back import execute
from vision.image_finder import find_image
from vision.screenshot import capture_region
from vision.ocr import read_image
from utils.drag_screen import forward,backward, down
from database.supabase_db import get_user_settings


def run(username):
    #pause for 2 sec
    Logger.log("confirming Home Screen")
    time.sleep(1)   
    
    #----------------------------------
    # cehcking if we are at home or not
    #----------------------------------
    def verify_home():

        for i in range(1,5):
            location_map = find_image(f"images/kingdom_map_{i}.png")
            if location_map:
                return location_map
             
            

    location_map = verify_home()

    if not location_map:
        truf_map = find_image("images/truf_map.png")
        if truf_map:
            pyautogui.click(truf_map)
        
        else:
            execute()

        time.sleep(2)

        location_map = verify_home()
    Logger.log("Truf verified")
    #----------------------------------
    # searching for barracks
    #----------------------------------

    Logger.log("Looking for Barracks")
    time.sleep(2)

    def find_barracks():
    
        for i in range(1, 11):
            location_barracks = find_image(f"images/barracks_{i}.png")
            if location_barracks:
                return location_barracks
        return None


    pattern = random.choice([forward(), backward()])

    for move in pattern:
        move()
        time.sleep(1)
        location_barracks = find_barracks()
        if location_barracks:
            break


    if location_barracks:
            Logger.log("Barracks Found")

            pyautogui.click(location_barracks)

            Logger.log("Barracks opened")
            
        
            #----------------------------
            # checking if trainng stats
            #----------------------------
            time.sleep(1)

            # training_stats = capture_region(
            #         745,
            #         150,
            #         150,
            #         51   
            #     )
            troop_type = None

            # training_stats = read_image(training_stats)
            # Logger.log(training_stats)

            idle = find_image(
                "images/training_idle.png"
            )
            running = find_image(
                "images/training_close.png"
            )

            if running:
                    # text = " ".join(training_stats)
                    # if re.search(r"\d",text):
                        Logger.log("Training going On")
                        execute()
                        return


            if idle:
                    Logger.log("No training Running")
    
                    settings = get_user_settings(username)
                    troop = settings["train_troop"]

                    Logger.log(f"Selected troops : {troop}")

                    troop_type = find_image(
                        f"images/{troop}.png"
                    )

                    if troop_type:
                        pyautogui.click(troop_type)
                        Logger.log("Troops Selected")

                    else:
                        for _ in range(3): #scroll down 3 times

                            down()
                            time.sleep(1)

                            troop_type = find_image(
                                f"images/{troop}.png"
                            )

                            if troop_type:
                                pyautogui.click(troop_type)
                                Logger.log("Troop Selected")
                                break

            #------------------------------------
            # starting new batch of training
            # -----------------------------------            
            if troop_type:
                time.sleep(1)
                amount = find_image("images/amount_selection.png")
                pyautogui.moveTo(amount)
                time.sleep(0.1)
                pyautogui.mouseDown()
                pyautogui.dragRel(        
                    400,
                    0,
                    duration=0.5,                     
                )
                pyautogui.mouseUp()
                time.sleep(1)
                pyautogui.click(865,525)
                time.sleep(1)
                change_gear = find_image("images/change_gear.png")

                if change_gear:
                    time.sleep(1)
                    pyautogui.click(change_gear)
                    time.sleep(1)
                    apply_gear = find_image("images/apply_gear.png")
                    time.sleep(1)
                    pyautogui.click(apply_gear)
                    time.sleep(2)
                    pyautogui.click(865,525)
                
                use_rss = find_image(
                     "images/use_rss.png"
                )
                if use_rss:
                     pyautogui.click(use_rss)
                     time.sleep(2)
                
                Logger.log(f"Training of {troop_type} started")
            execute()
            time.sleep(1)
            execute()

            if not troop_type:
                 Logger.log("Selected troop not found")
                 execute()