class calculator:
    """A Calculator"""

    def __init__(self, arr) -> None:
        """Calculator constructor"""
        self.arr = arr

    def __add__(self, object) -> None:
        """Addition operator overload"""
        self.arr = [ele + object for ele in self.arr]
        print(self.arr)

    def __mul__(self, object) -> None:
        """Multiplication operator overload"""
        self.arr = [ele * object for ele in self.arr]
        print(self.arr)

    def __sub__(self, object) -> None:
        """Subtraction operator overload"""
        self.arr = [ele - object for ele in self.arr]
        print(self.arr)

    def __truediv__(self, object) -> None:
        """Division operator overload"""
        if object == 0:
            raise ZeroDivisionError("Division by zero")
        self.arr = [ele / object for ele in self.arr]
        print(self.arr)
