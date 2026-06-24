import pyautogui
import time

# Center of your 1024x576 game

CENTER_X = 513
CENTER_Y = 307


def left():

    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )

    time.sleep(0.2)

    pyautogui.dragRel(
        256,
        0,
        duration=0.5,
        button="left"
    )
    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )


def right():

    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )

    time.sleep(0.2)

    pyautogui.dragRel(
        -256,
        0,
        duration=0.5,
        button="left"
    )
    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )


def up():

    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )

    time.sleep(0.2)

    pyautogui.dragRel(
        0,
        288,
        duration=0.5,
        button="left"
    )
    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )


def down():

    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )

    time.sleep(0.2)

    pyautogui.dragRel(
        0,
        -288,
        duration=0.5,
        button="left"
    )
    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )