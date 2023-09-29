def square(x: int | float) -> int | float:
	"""Return the square of a number"""
	return x ** 2


def pow(x: int | float) -> int | float:
	"""Return the result of pow(x, x)"""
	return x ** x


def outer(x: int | float, function) -> object:
	"""Return a closure that
		- keep track of the amount of times it was called,
		- redefine x with the result of function(x),
		- and return the result of function(x) every call
	"""

	count = 0
	def inner() -> float:
		"""The closure"""
		nonlocal count
		nonlocal x

		count += 1
		x = function(x)
		return x
	return inner
