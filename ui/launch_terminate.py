import subprocess
import time
import pygetwindow as gw

def position_game():
    windows = gw.getWindowsWithTitle(
    "Lords Mobile PC"
    )
    if not windows:
        return False
    
    game = windows[0]
    game.restore()
    game.moveTo(
        0,0
    )
    game.resizeTo(
        1026,615
    )
    game.activate()
    return True

def launch():
    #launch the application
    subprocess.Popen(["C:\\Users\\ronak_8q45q08\\AppData\\Roaming\\IGG\\Lords Mobile PC\\Lords Mobile Updater.exe"])

#terminate the application


def kill_process_by_name(Lords = "Lords Mobile PC.exe"):
    # Example process_name: 'notepad.exe' or 'chrome.exe'
    try:
        # /F forces the process to close, /IM specifies the image name
        subprocess.run(['taskkill', '/F', '/IM', Lords], check=True)
        print(f"Successfully killed process: {Lords}")
    except subprocess.CalledProcessError:
        print(f"Failed to kill or process not found: {Lords}")

