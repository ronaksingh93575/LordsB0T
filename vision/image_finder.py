import cv2
import numpy as np
import pyautogui


def find_image(
        image_path,
        confidence=0.7
):

    screenshot = pyautogui.screenshot()

    screenshot = np.array(
        screenshot
    )

    screenshot = cv2.cvtColor(
        screenshot,
        cv2.COLOR_RGB2BGR
    )

    template = cv2.imread(
        image_path
    )

    result = cv2.matchTemplate(
        screenshot,
        template,
        cv2.TM_CCOEFF_NORMED
    )

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(
        result
    )

    if max_val >= confidence:

        height, width = template.shape[:2]

        center_x = max_loc[0] + width // 2

        center_y = max_loc[1] + height // 2

        return (
            center_x,
            center_y
        )

    return None