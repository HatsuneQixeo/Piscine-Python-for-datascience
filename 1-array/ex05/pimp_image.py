from PIL import Image
import numpy as np


def get_extension(filename: str) -> str | None:
    """Return the extension of the given filename, None if not found"""

    extension_pos = filename.rfind('.')
    if extension_pos == -1:
        return None
    else:
        return filename[extension_pos + 1:]


# This whole thing is basically a waste of time.
#
# Exporting images should never be these functions responsibility in practice.
#
# If we just left the actual program to decide,
# it's as easy as just extracting the extension from the source.
#
# That said, I wonder what stopped me from exporting images as png.
def export_image(data: np.ndarray, filename: str, format: str | None = None) \
        -> None:
    """Decides the extension if not specified either in filename or format

    Args:
        data (np.ndarray): Image data
        filename (str): Filename to save the image
        format (str, optional): Format of the image. (jpg, png, etc.)

    Fill in filename's extension if not included,
    or fill in format with filename's extension format is None.
    If both filename and format are empty,
    then the extension will be defaulted to jpg.
    """

    assert isinstance(filename, str), "Invalid filename type"
    # 2d array can be interpreted as black and white by PIL
    assert data.ndim in (2, 3), "Invalid data dimensions"
    extension = get_extension(filename)
    if format is None:
        if extension == "jpg":  # format= does not recognize "jpg"
            format = "jpeg"
        elif extension:  # if extension is not empty nor None
            format = extension
        # if each pixels has 4 channels(RGBA)
        elif data.ndim == 3 and data.shape[2] == 4:
            format = "png"
        else:  # default as jpeg
            format = "jpeg"
    assert isinstance(format, str), "Format is not string"
    assert format.find('.') == -1, "Format should not include ."
    if extension is None:
        filename = f"{filename}.{format}"
    Image.fromarray(data).save(filename, format)


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the array's rgb values"""
    array = array.copy()
    array[:, :, :3] = 255 - array[:, :, :3]
    export_image(array, "inverted")
    return array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Filter green and blue channels from the array"""
    array = array.copy()
    array[:, :, (1, 2)] = 0
    export_image(array, "red")
    return array


def ft_green(array: np.ndarray) -> np.ndarray:
    """Filter red and blue channels from the array"""
    array = array.copy()
    array[:, :, (0, 2)] = 0
    export_image(array, "green")
    return array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Filter red and green channels from the array"""
    array = array.copy()
    array[:, :, (0, 1)] = 0
    export_image(array, "blue")
    return array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Greyscale the array's rgb channels"""
    array = array.copy()
    # greyscaled = array[:, :, :3].mean(2)
    greyscaled = array[:, :, :3].dot((.299, .587, .114))
    array[:, :, :3] = greyscaled[:, :, np.newaxis]
    export_image(array, "grey")
    return array


# def ft_cyan(array: np.ndarray) -> np.ndarray:
#     """Filter red channel from the array"""
#     array = array.copy()
#     array[:, :, 0] = 0
#     Image.fromarray(array).save("cyan.jpg")
#     return array


# def ft_magenta(array: np.ndarray) -> np.ndarray:
#     """Filter green channel from the array"""
#     array = array.copy()
#     array[:, :, 1] = 0
#     Image.fromarray(array).save("magenta.jpg")
#     return array


# def ft_yellow(array: np.ndarray) -> np.ndarray:
#     """Filter blue channel from the array"""
#     array = array.copy()
#     array[:, :, 2] = 0
#     Image.fromarray(array).save("yellow.jpg")
#     return array
