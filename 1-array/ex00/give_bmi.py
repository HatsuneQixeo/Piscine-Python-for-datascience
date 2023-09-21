import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Returns a list of BMI values given a list of height and weight.
This function expects height in meters(m) and weight in kilograms(kg)."""

    np_height = np.array(height)
    np_weight = np.array(weight)
    assert np_height.size == np_weight.size, \
        "height and weight must have the same length"
    assert np_height.dtype in (np.dtype('int'), np.dtype('float')), \
        "height must be a list of numbers"
    assert np_weight.dtype in (np.dtype('int'), np.dtype('float')), \
        "weight must be a list of numbers"
    return (np_weight / (np_height ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of boolean value \
representing whether the BMI is beyond the given limit."""

    arr = np.array(bmi)
    assert arr.dtype in (np.dtype('int'), np.dtype('float')), \
        "bmi must be a list of numbers"
    return (arr > limit).tolist()


# def give_bmi(height: list[int | float], weight: list[int | float]) \
#         -> list[int | float]:
#     """Returns a list of BMI values given a list of height and weight.
# This function expects height in meters(m) and weight in kilograms(kg)."""

#     assert len(height) == len(weight), \
#         "height and weight must have the same length"
#     assert all(isinstance(ele, (int, float)) for ele in height), \
#         "height must be a list of numbers"
#     assert all(isinstance(ele, (int, float)) for ele in weight), \
#         "weight must be a list of numbers"
#     return [w / (h ** 2) for h, w in zip(height, weight)]


# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#     """Return a list of boolean value \
# representing whether the BMI is beyond the given limit."""

#     assert all(isinstance(ele, (int | float)) for ele in bmi), \
#         "bmi must be a list of numbers"
#     return [ele > limit for ele in bmi]
