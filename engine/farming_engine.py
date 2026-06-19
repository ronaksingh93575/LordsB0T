import sys
import os
# 
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


import threading
import time
from utils.logger import Logger
from tasks.close_bundle import run as close_bundle
from ui.launch_terminate import position_game
from database.supabase_db import get_user_settings
from tasks import check_shield





class FarmingEngine:

    def __init__(self, username , logcallback=None):


        self.username = username
        self.running = False
        self.thread = None
        self.log_callback = logcallback

    def bot_loop(self):

        while self.running:
            
            if not self.running:
                break

            #--------------------------------
            # Window Set up
            #--------------------------------
            Logger.log("Setting Up things")
            position_game()
            time.sleep(2)

            Logger.log("Adjusted Location and size..")
            time.sleep(2)

            Logger.log("Searching bundle popup...")
            close_bundle()
            time.sleep(2)

            if not self.running:
                break

            #------------------------------------
            # shielding
            #------------------------------------

            settings = get_user_settings(
                self.username
            )

            if settings["check_shield"]:
                check_shield.run(
                    self.username
                )
            
            time.sleep(2)

            if not self.running:
                break            

            #------------------------------------
            # shielding
            #------------------------------------    
                    
            print("Sending troops...")

            time.sleep(2)

            if not self.running:
                break            

            #------------------------------------
            # shielding
            #------------------------------------    
                    
            print("Gathering resources...")

            time.sleep(2)

    def start(self):

        if not self.running:

            self.running = True

            self.thread = threading.Thread(
                target=self.bot_loop,
                daemon=True
            )

            self.thread.start()

    def stop(self):

        self.running = False

        Logger.log("Farming Engine Stopping...")

    def log(self, message):

        if self.log_callback:
        
            self.log_callback(message)
# print(type(Logger))