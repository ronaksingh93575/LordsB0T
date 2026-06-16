import easyocr

reader = easyocr.Reader(
    ['en'],
    gpu=False
)


def read_text(image_path):

    result = reader.readtext(
        image_path,
        detail=0
    )

    return result