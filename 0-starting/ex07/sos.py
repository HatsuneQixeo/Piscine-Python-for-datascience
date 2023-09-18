import sys


def morse(string: str) -> str:
    """Translate a string into morse code"""

    NESTED_MORSE = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '/'
    }

    return ' '.join([NESTED_MORSE.get(i.upper()) for i in string])


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        string = sys.argv[1]
        assert string.replace(' ', '').isalnum(), "the arguments are bad"
        print(morse(string))
        exit(0)
    except AssertionError as e:
        print("AssertionError:", e)
    except BaseException as e:
        print(e)
    exit(1)


if __name__ == "__main__":
    main()
