import numpy as NumPy


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a list using numpy, and log the difference in stdout"""

    assert isinstance(family, list), "family must be a list"

    arr = NumPy.array(family)[slice(start, end)]
    print("My shape is :", NumPy.shape(family))
    print("My new shape is :", arr.shape)
    return arr.tolist()
