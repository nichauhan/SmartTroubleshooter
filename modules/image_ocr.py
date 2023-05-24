import pytesseract
import imageio.v3 as iio

def get_image_text(image):
    """
    Takes in the Image uploaded by the user and extracts the text from that image
    """
    text = pytesseract.image_to_string(iio.imread(image))
    return text