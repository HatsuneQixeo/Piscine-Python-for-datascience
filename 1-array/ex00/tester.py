from give_bmi import give_bmi, apply_limit
import numpy as np


def subjectTest():
    """Test case given by subject"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


def testExcept(height: list, weight: list, throw: bool) -> str:
    """Component for Exception testing"""
    try:
        lst_bmi = give_bmi(height, weight)
        lst_limit = apply_limit(lst_bmi, 26)
        print(lst_bmi)
        print(lst_limit)
        if throw:
            return "Missing Exception"
    except Exception as e:
        print(f"{e.__class__.__name__}:", e)
        if not throw:
            return f"Unexpected Exception({e.__class__.__name__})"
    return ""


def test(height: list, weight: list, throw: bool) -> None:
    """Test whether the exception is thrown correctly"""
    reset = '\x1b[0m'
    bold = '\x1b[1m'
    red_text = '\x1b[31m'
    green_text = '\x1b[32m'
    error = testExcept(height, weight, throw)
    if error:
        print(f"Error: {error} for case:", height, weight)
        print(f"{bold}{red_text}Failed{reset}")
    else:
        print(f"{bold}{green_text}OK{reset}")


def mytest():
    """Test cases for exceptions"""
    print("test: int and float")
    test([1, 1.8, 1.9], [60, 70, 80], False)

    print("test: contain str")
    test([1, 1.8, "str"], [60, 70, 80], True)

    # Note: bool is a subclass of int
    print("test: contain bool")
    test([1, 1.8, True], [60, 70, 80], False)

    print("test: different length")
    test([1, 1.8, 1.9], [60, 70], True)

    print("test: contain None")
    test([1, 1.8, 1.9], [60, 70, None], True)

    print("test: empty list")
    test([], [], False)

    print("test: 2d list")
    test([[1.9, 1.8], [1.7, 1.9]], [[50, 60], [70, 99]], False)

    print("test: different shape")
    test([[1.9, 1.8], [19, 11]], [50, 60, 11, 99], True)

    print("test: weird shape")
    test([[1.9, 1.8], [19]], [50, 60], True)

    # Technically the rest of the test are not list so...
    # The only test where it matters is probably float/complex128,
    # where the type is still being kept track by list.
    # Based on the result of asserting issubclass(arr.dtype.type, (int, float))
    #  inside apply_limit
    a = np.array([1, 2])

    cast = lambda type: a.astype(type).tolist()
    print("test: type float16/32")
    test(a.astype(np.float16).tolist(), a.astype(np.float32).tolist(), False)
    print("test: type float64/128")
    test(a.astype(np.float64).tolist(), a.astype(np.float128).tolist(), False)

    print("test: type int8/16")
    test(a.astype(np.int8).tolist(), a.astype(np.int16).tolist(), False)
    print("test: type int32/64")
    test(a.astype(np.int32).tolist(), a.astype(np.int64).tolist(), False)

    print("test: type uint8/16")
    test(a.astype(np.uint8).tolist(), a.astype(np.uint16).tolist(), False)
    print("test: type uint32/64")
    test(a.astype(np.uint32).tolist(), a.astype(np.uint64).tolist(), False)

    print("test: type np.bool_")
    test(a.astype(np.bool_).tolist(), a.astype(np.bool_).tolist(), True)

    print("test: type complex64")
    test(a.astype(np.complex64).tolist(), a.astype(np.complex64).tolist(), False)
    print("test: type complex128")
    test(a.astype(np.complex128).tolist(), a.astype(np.complex128).tolist(), False)




def main():
    try:
        subjectTest()
        mytest()
    except Exception as e:
        # print(f"Unexpected {e.__class__.__name__} in main:", e)
        raise e


if __name__ == "__main__":
    main()
