from PIL import Image
import numpy as np
from load_image import ft_load


def arrSlice(array: np.ndarray, x_pos: int, y_pos: int, length: int) \
        -> np.ndarray:
    """Slices the array as square"""
    return array[y_pos:(y_pos + length), x_pos:(x_pos + length)]


def arrTranspose(arr: np.ndarray) -> np.ndarray:
    """Transpose the array"""
    return np.array([ele for ele in zip(*arr)])


def main():
    try:
        array = ft_load("../assets/animal.jpeg")
        print(array)
        arr_transposed = arrTranspose(arrSlice(array, 450, 100, 400))
        print("New shape after Transpose:", arr_transposed.shape)
        print(arr_transposed)
        Image.fromarray(arr_transposed).save("transpose270.jpg")
    except Exception as e:
        print(f"{e.__class__.__name__}:", e)
        exit(1)


if __name__ == "__main__":
    main()
