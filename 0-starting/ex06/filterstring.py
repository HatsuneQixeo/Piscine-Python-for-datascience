import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        string = sys.argv[1]
        if string == "":
            return
        elif not string.isprintable():
            raise AssertionError("Contain non printable characters")
        elif not string.replace(' ', '').isalnum():
            raise AssertionError("Contain punctuation characters")
        n = int(sys.argv[2])
        print(list(ft_filter(lambda x: len(x) > n, string.split())))
        return
    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(e)
    exit(1)


if __name__ == "__main__":
    main()
