
import sys


def get_morse(code: str):
	NESTED_MORSE = {
		'.-': 'A',
		'-...': 'B',
		'-.-.': 'C',
		'-..': 'D',
		'.': 'E',
		'..-.': 'F',
		'--.': 'G',
		'....': 'H',
		'..': 'I',
		'.---': 'J',
		'-.-': 'K',
		'.-..': 'L',
		'--': 'M',
		'-.': 'N',
		'---': 'O',
		'.--.': 'P',
		'--.-': 'Q',
		'.-.': 'R',
		'...': 'S',
		'-': 'T',
		'..-': 'U',
		'...-': 'V',
		'.--': 'W',
		'-..-': 'X',
		'-.--': 'Y',
		'--..': 'Z',
		'-----': '0',
		'.----': '1',
		'..---': '2',
		'...--': '3',
		'....-': '4',
		'.....': '5',
		'-....': '6',
		'--...': '7',
		'---..': '8',
		'----.': '9',
		'/': ' ',
	}

	letter = NESTED_MORSE.get(code)
	if letter:
		return (letter, False)
	else:
		return (code, True)


def to_morse(line: str):
	words = line.split()
	if len(words) == 0:
		return ''
	translated = [get_morse(word) for word in words]
	msg, prev_type = translated[0]
	for word, type in translated[1:]:
		msg += (' ' + word) if (type or prev_type) else (word)
		prev_type = type
	return msg


def main():
	try:
		if len(sys.argv) == 1:
			args = [line.strip('\n') for line in sys.stdin]
			delimiter = '\n'
		else:
			args = sys.argv[1:]
			delimiter = ' '
		print(delimiter.join([to_morse(line) for line in args]))
	except KeyboardInterrupt:
		exit(130)
	except Exception as e:
		print('Error:', e)
		exit(1)


if __name__ == "__main__":
	main()
