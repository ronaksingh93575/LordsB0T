import easyocr
import numpy as np

reader = easyocr.Reader(
    ['en'],
    gpu=False
)


def read_image(image):

    image = np.array(image)

    return reader.readtext(
        image,
        detail=0
    )