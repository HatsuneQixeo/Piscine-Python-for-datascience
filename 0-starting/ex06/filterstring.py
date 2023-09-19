import sys
from ft_filter import ft_filter


def main():
    try:
        if not (len(sys.argv) == 3 and sys.argv[2].isdigit()):
            raise AssertionError("the arguments are bad")
        string = sys.argv[1]
        if not string.isprintable():
            raise AssertionError("Contain non printable characters")
        if not string.replace(' ', '').isalnum():
            raise AssertionError("Contain punctuation characters")
        n = int(sys.argv[2])
        print([i for i in ft_filter(lambda x: len(x) > n, string.split())])
        exit(0)
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print(e)
    exit(1)


if __name__ == "__main__":
    main()
