import numpy as NumPy


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Returns a list of BMI values given a list of height and weight.
This function expects height in meters(m) and weight in kilograms(kg)."""

    np_height = NumPy.array(height)
    np_weight = NumPy.array(weight)
    if np_height.size != np_weight.size:
        raise IndexError("height and weight must have the same length")
    elif np_height.dtype not in (NumPy.dtype('int'), NumPy.dtype('float')):
        raise TypeError("height must be a list of numbers")
    elif np_weight.dtype not in (NumPy.dtype('int'), NumPy.dtype('float')):
        raise TypeError("weight must be a list of numbers")
    else:
        return (np_weight / (np_height ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of boolean value \
representing whether the BMI is beyond the given limit."""

    arr = NumPy.array(bmi)
    if arr.dtype not in (NumPy.dtype('int'), NumPy.dtype('float')):
        raise TypeError("bmi must be a list of numbers")
    else:
        return (arr > limit).tolist()


# def give_bmi(height: list[int | float], weight: list[int | float]) \
#         -> list[int | float]:
#     """Returns a list of BMI values given a list of height and weight.
# This function expects height in meters(m) and weight in kilograms(kg)."""

#     if len(height) != len(weight):
#         raise IndexError("height and weight must have the same length")
#     elif not all(isinstance(ele, (int, float)) for ele in height):
#         raise TypeError("height must be a list of numbers")
#     elif not all(isinstance(ele, (int, float)) for ele in weight):
#         raise TypeError("weight must be a list of numbers")
#     else:
#         return [w / (h ** 2) for h, w in zip(height, weight)]


# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#     """Return a list of boolean value \
# representing whether the BMI is beyond the given limit."""

#     if not all(isinstance(ele, (int | float)) for ele in bmi):
#         raise TypeError("bmi must be a list of numbers")
#     else:
#         return [ele > limit for ele in bmi]
