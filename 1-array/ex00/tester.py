from give_bmi import give_bmi, apply_limit


def subjectTest():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


def testException(height: list, weight: list, throw: bool) -> str:
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
    reset = '\x1b[0m'
    bold = '\x1b[1m'
    red_text = '\x1b[31m'
    green_text = '\x1b[32m'
    error = testException(height, weight, throw)
    if error:
        print(f"Error: {error} for case:", height, weight)
        print(f"{bold}{red_text}Failed{reset}")
    else:
        print(f"{bold}{green_text}OK{reset}")


def mytest():
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


def main():
    try:
        subjectTest()
        mytest()
    except Exception as e:
        print("Unexpected Exception in main:", e)


if __name__ == "__main__":
    main()
