class calculator:
    """A Calculator"""

    def __init__(self, arr) -> None:
        self.arr = arr

    def __add__(self, object) -> None:
        self.arr = [ele + object for ele in self.arr]
        print(self.arr)

    def __mul__(self, object) -> None:
        self.arr = [ele * object for ele in self.arr]
        print(self.arr)

    def __sub__(self, object) -> None:
        self.arr = [ele - object for ele in self.arr]
        print(self.arr)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise ZeroDivisionError("Division by zero")
        self.arr = [ele / object for ele in self.arr]
        print(self.arr)
