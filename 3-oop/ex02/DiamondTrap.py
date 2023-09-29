from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A King that inherits from both Baratheon and Lannister"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """King constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = Baratheon.family_name
        self.eyes = Baratheon.eyes
        self.hairs = Baratheon.hairs

    def set_eyes(self, eyes: str) -> None:
        """Set eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """Set hairs"""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """Get eyes"""
        return self.eyes

    def get_hairs(self) -> str:
        """Get hairs"""
        return self.hairs
