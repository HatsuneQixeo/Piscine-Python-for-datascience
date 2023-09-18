import sys
from ft_filter import ft_filter

def main():
    try:
        assert len(sys.argv) == 3 and sys.argv[2].isdigit(), \
            "the arguments are bad"
        string = sys.argv[1]
        assert string.isprintable(), \
            "Contain non printable characters"
        assert string.replace(' ', '').isalnum(), \
            "Contain punctuation characters"
        n = int(sys.argv[2])
        print([i for i in ft_filter(lambda x: len(x) > n, string.split())])
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
    except BaseException as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
