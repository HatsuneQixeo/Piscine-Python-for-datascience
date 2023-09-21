from give_bmi import give_bmi, apply_limit
import numpy as np


def subjectTest():
    """Test case given by subject"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


def testExcept(height: list, weight: list, e_class: type[Exception]) -> str:
    """Component for Exception testing"""
    assert (e_class is None or issubclass(e_class, Exception)), \
        "e_class must be a type or None"
    try:
        lst_bmi = give_bmi(height, weight)
        lst_limit = apply_limit(lst_bmi, 26)
        print(lst_bmi)
        print(lst_limit)
        if e_class is not None:
            return f"Missing {e_class.__name__}"
    except Exception as e:
        print(f"{e.__class__.__name__}:", e)
        if e_class is not e.__class__:
            return f"Unexpected {e.__class__.__name__}, \
expected {e_class.__name__ if e_class is not None else 'None'}"
    return ""


def test(height: list, weight: list, exception: type[Exception] = None) \
        -> None:
    """Test whether the exception is thrown correctly"""
    reset = '\x1b[0m'
    bold = '\x1b[1m'
    red_text = '\x1b[31m'
    green_text = '\x1b[32m'
    error = testExcept(height, weight, exception)
    if error:
        print(f"Error: {error} for case:", height, weight)
        print(f"{bold}{red_text}Failed{reset}")
    else:
        print(f"{bold}{green_text}OK{reset}")


def mytest():
    """Test cases for exceptions"""
    print("test: int and float")
    test([1, 1.8, 1.9], [60, 70, 80])

    # Note: bool is a subclass of int
    print("test: contain bool")
    test([1, 1.8, False], [60, 70, 80])

    print("test: empty list")
    test([], [])

    print("test: 2d list")
    test([[1.9, 1.8], [1.7, 1.9]], [[50, 60], [70, 99]])

    print("test: contain str")
    test([1, 1.8, "str"], [60, 70, 80], AssertionError)

    print("test: different length")
    test([1, 1.8, 1.9], [60, 70], AssertionError)

    print("test: contain None")
    test([1, 1.8, 1.9], [60, 70, None], AssertionError)

    print("test: different shape")
    test([[1.9, 1.8], [19, 11]], [50, 60, 11, 99], ValueError)

    print("test: weird shape")
    test([[1.9, 1.8], [19]], [50, 60], ValueError)

    # Technically the rest of the test are not list so...
    # The only test where it matters is probably float/complex128,
    # where the type is still being kept track by list.
    # Based on the result of asserting issubclass(arr.dtype.type, (int, float))
    #  inside apply_limit
    a = np.array([1, 2])

    # flake8 sucks
    def cast(type: np.dtype) -> list:
        return a.astype(type).tolist()
    # cast = lambda type: a.astype(type).tolist()

    print("test: type float16/32")
    test(cast(np.float16), cast(np.float32))
    print("test: type float64/128")
    test(cast(np.float64), cast(np.float128))

    print("test: type int8/16")
    test(cast(np.int8), cast(np.int16))
    print("test: type int32/64")
    test(cast(np.int32), cast(np.int64))

    print("test: type uint8/16")
    test(cast(np.uint8), cast(np.uint16))
    print("test: type uint32/64")
    test(cast(np.uint32), cast(np.uint64))

    print("test: type complex64/128")
    test(cast(np.complex64), cast(np.complex128))

    print("test: type np.bool_")
    test(cast(np.bool_), cast(np.bool_), AssertionError)


def main():
    subjectTest()
    mytest()


if __name__ == "__main__":
    main()
