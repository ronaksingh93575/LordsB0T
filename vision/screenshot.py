import pyautogui


def take_screenshot():

    screenshot = pyautogui.screenshot()

    return screenshot

def capture_region(
        x,
        y,
        width,
        height,
):
    return  pyautogui.screenshot(
        region=(
            x,
            y,
            width,
            height
        )
    )


#     screenshot = pyautogui.screenshot(
#         region=(
#             x,
#             y,
#             width,
#             height
#         )
#     )
#     return screenshot

# image = capture_region(
#                     745,
#                     150,
#                     150,
#                     51 
# )
# image.save(
#     "temp/x.png"
# )