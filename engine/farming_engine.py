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
from ui.settings import SettingsWindow





class FarmingEngine:

    def __init__(self, logcallback=None):

        self.running = False
        self.thread = None
        self.logcallback = logcallback

    def bot_loop(self):

        while self.running:

            Logger.log("Setting Up things")
            position_game()
            Logger.log("Adjusted Location and size..")

            Logger.log("Searching bundle popup...")
            close_bundle()

            time.sleep(5)

            # if SettingsWindow["check_shield"]:
                # check_shield.run()

            print("Sending troops...")

            time.sleep(5)

            print("Gathering resources...")

            time.sleep(5)

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

    def log(self, message):

        if self.log_callback:
        
            self.log_callback(message)
# print(type(Logger))