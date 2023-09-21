import numpy as np


def slice_me(family: list[int], start: int, end: int) -> list:
    """Slice a list using numpy, and log the difference in shape to stdout"""

    assert isinstance(family, list), "family must be a list"

    np_family = np.array(family)
    arr = np_family[slice(start, end)]
    print("My shape is :", np_family.shape)
    print("My new shape is :", arr.shape)
    return arr.tolist()

    # arr = family[start:end]
    # print("My shape is :", np.shape(family))
    # print("My new shape is :", np.shape(arr))
    # return arr
