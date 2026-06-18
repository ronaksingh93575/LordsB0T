import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from vision.screenshot import capture_region
from vision.ocr import read_image

image = capture_region(
    120,
    292,
    650,
    60,
)
result = read_image(
    image
)
print(result)