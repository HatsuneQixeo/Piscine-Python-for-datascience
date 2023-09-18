import sys


def add(counts: dict, c: str):
    """building's helper function"""

    funcset = {
        c.isupper: 'upper',
        c.islower: 'lower',
        c.isspace: 'space',
        c.isdigit: 'digit'
    }
    for f in funcset:
        if f():
            counts[funcset[f]] += 1
            return
    counts['other'] += 1


def building(string: str):
    """Prints the length of the string and the amount of each character type"""

    counts = {
        'upper': 0,
        'lower': 0,
        'space': 0,
        'digit': 0,
        'other': 0
    }

    assert string.isprintable(), f'Contains non-printable character: {string}'
    for c in string:
        add(counts, c)
    print(f'The text contains {len(string)} characters:')
    print(f'{counts["upper"]} upper letters')
    print(f'{counts["lower"]} lower letters')
    print(f'{counts["other"]} punctuation marks')
    print(f'{counts["space"]} spaces')
    print(f'{counts["digit"]} digits')


def main():
    length = len(sys.argv)
    try:
        if length == 1:
            arg = input('Enter string: ')
        elif length == 2:
            arg = sys.argv[1]
        else:
            raise AssertionError("Too many arguments")
        building(arg)
    except AssertionError as e:
        print("AssertionError:", e)
    except BaseException as e:
        print(e)


if __name__ == '__main__':
    main()
