class calculator:
    """A vector calculator"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product of two vectors"""
        print("Dot product is:", sum(a * b for a, b in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition of two vectors"""
        print("Add Vector is :", [float(a + b) for a, b in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtraction of two vectors"""
        print("Sous Vector is:", [float(a - b) for a, b in zip(V1, V2)])
