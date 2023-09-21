from PIL import Image
import numpy as np
from load_image import ft_load


def arrSlice(array: np.ndarray, x_pos: int, y_pos: int, length: int) \
        -> np.ndarray:
    """Slices the array as square"""
    return array[y_pos:(y_pos + length), x_pos:(x_pos + length)]


def main():
    try:
        array = ft_load("../assets/animal.jpeg")
        arr_sliced = arrSlice(array, 450, 100, 400)

        print(array)
        print("The shape of the sliced array is: ", arr_sliced.shape)
        print(arr_sliced)
        Image.fromarray(arr_sliced).save("sliced.jpg")
    except Exception as e:
        print(f"{e.__class__.__name__}:", e)


if __name__ == "__main__":
    main()
