from PIL import Image
import numpy as np


def ft_load(path: str):
    """Loads an image as numpy array and prints its shape to stdout"""
    image = Image.open(path)
    array = np.array(image)
    print("The shape of image is: ", array.shape)
    return array
