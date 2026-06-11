from vision.image_finder import find_image
from vision.clicker import click


def run():

    location = find_image(
        "images/colosseum.png"
    )

    if location:

        click(
            location[0],
            location[1]
        )

        return True

    return False