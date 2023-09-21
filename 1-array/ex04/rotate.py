from PIL import Image
import numpy as np
from load_image import ft_load


def arrSlice(array: np.ndarray, x_pos: int, y_pos: int, length: int) \
        -> np.ndarray:
    """Slices the array as square"""
    return array[y_pos:(y_pos + length), x_pos:(x_pos + length)]


def arrTranspose(arr: np.ndarray) -> np.ndarray:
    """Transpose the array"""
    return np.array([[row[i] for row in arr] for i in range(len(arr[0]))])


def main():
    try:
        array = ft_load("../assets/animal.jpeg")
        arr_sliced = arrSlice(array, 450, 100, 400)
        print(array)
        arr_transposed = arrTranspose(arr_sliced)
        print("New shape after Transpose:", arr_transposed.shape)
        Image.fromarray(arr_transposed).save("transpose270.jpg")
    except Exception as e:
        print(f"{e.__class__.__name__}:", e)
        exit(1)


if __name__ == "__main__":
    main()
