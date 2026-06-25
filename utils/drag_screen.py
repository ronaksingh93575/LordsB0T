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

    time.sleep(0.1)
    pyautogui.mouseDown()
    pyautogui.moveRel(
        400,
        0,
        duration=0.5,    
        )
    time.sleep(0.1)
    pyautogui.mouseUp()
    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )
    

def right():

    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )

    time.sleep(0.1)
    pyautogui.mouseDown()
    pyautogui.dragRel(
        -250,
        0,
        duration=0.5,
    )
    time.sleep(0.1)
    pyautogui.mouseUp()
    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )


def up():

    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )

    time.sleep(0.1)
    pyautogui.mouseDown()
    pyautogui.dragRel(
        0,
        100,
        duration=0.5,
    )
    time.sleep(0.1)
    pyautogui.mouseUp()
    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )

def down():

    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )

    time.sleep(0.1)
    pyautogui.mouseDown()
    pyautogui.dragRel(
        0,
        -100,
        duration=0.5,
    )
    time.sleep(0.1)
    pyautogui.mouseUp()
    pyautogui.moveTo(
        CENTER_X,
        CENTER_Y
    )


def forward():
    [
            up, up, up,up,
            left,left,left,left,
            down,
            right,right,right,right,right,right,
            down,
            left, left, left, left,left,left,left,
            down,
            right,right,right,right,right,right,
            down,
            left, left, left, left,left,left,left,
            down,
            right,right,right,right,right,right,
            down,
            left, left, left, left,left,left,left,
            down,
        ]

def backward(): 
     [

        up,
        right, right, right, right, right, right, right,
        up,
        left, left, left, left, left, left,
        up,
        right, right, right, right, right, right, right,
        up,
        left, left, left, left, left, left,
        up,
        right, right, right, right, right, right, right,
        up,
        left, left, left, left,
        down, down, down, down
    ]