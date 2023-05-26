import pytesseract
from PIL import Image
import imageio.v3 as iio


def get_image_text(image):
    """
    Takes in the Image uploaded by the user and extracts the text from that image
    """
    text = pytesseract.image_to_string(iio.imread(image), lang='eng')
    return text


if __name__ == '__main__':
    image_path = ""

    im = Image.open(image_path)

    image_text = get_image_text(im)
    print(image_text)
