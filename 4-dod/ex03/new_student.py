import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates random id"""

    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student"""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Generates login from name and surname"""
        self.login = (self.name[0] if self.name else '') + self.surname
