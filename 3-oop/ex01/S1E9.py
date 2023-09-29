from abc import ABC, abstractmethod


class Character(ABC):
    """An abscract class that represents a character"""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Character Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """Omae wa mou shindeiru"""
        self.is_alive = False


class Stark(Character):
    """A stark family that inherits from Character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Stark Constructor"""
        Character.__init__(self, first_name, is_alive)
