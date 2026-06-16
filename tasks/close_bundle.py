import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from utils.logger import Logger
from vision.image_finder import find_image
from vision.clicker import click


def run():

    Logger.log(
        "Searching bundle popup..."
    )

    location = find_image(
        "images/close_bundle.png"
    )

    if location:

        click(
            location[0],
            location[1]
        )

        Logger.log(
            "Bundle popup closed."
        )

        return True

    Logger.log(
        "Bundle popup not found."
        )

    return False