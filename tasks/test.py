import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from vision.image_finder import find_image
from vision.clicker import click

location = find_image(
    "images/close_bundle.png"
)

if location:

    click(
        location[0],
        location[1]
    )

    print("Clicked")

else:

    print("Not Found")
