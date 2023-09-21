import sys


def add(counts: dict, c: str) -> bool:
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
            return True
    return False


def building(string: str):
    """Prints the length of the string and the amount of each character type"""

    counts = {
        'upper': 0,
        'lower': 0,
        'space': 0,
        'digit': 0,
        'other': 0
    }

    for c in string:
        if add(counts, c):
            continue
        elif c.isprintable():
            counts['other'] += 1
        else:
            raise AssertionError(f'Contain non-printable character: {string}')
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
            print("Enter a string:", end=' ', flush=True, file=sys.stderr)
            arg = sys.stdin.readline()
        elif length == 2:
            arg = sys.argv[1]
        else:
            raise AssertionError("Too many arguments")
        building(arg)
        exit(0)
    except AssertionError as e:
        print("AssertionError:", e)
    except KeyboardInterrupt:
        pass
    exit(1)


if __name__ == '__main__':
    main()
