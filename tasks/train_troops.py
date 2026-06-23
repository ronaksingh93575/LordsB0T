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
from ui import settings


def run(username):
    #pause for 2 sec
    Logger.log("confirming Home Screen")
    time.sleep(1)

    