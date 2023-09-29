from S1E9 import Character


class Baratheon(Character):
    """A Baratheon family that inherits from Character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        """String representation of the Baratheon class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Object representation of the Baratheon class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """A Lannister family that inherits from Character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create Lannister"""
        return cls(first_name, is_alive)

    def __str__(self) -> str:
        """String representation of the Lannister class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Object representation of the Lannister class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
