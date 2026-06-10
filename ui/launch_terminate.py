import subprocess
import time

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

