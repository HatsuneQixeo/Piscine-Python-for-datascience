from S1E7 import Baratheon, Lannister
from S1E9 import Character, Stark
from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
if (isinstance(Joffrey, King)
    and issubclass(King, Character)
    and isinstance(Joffrey, Baratheon)
    and isinstance(Joffrey, Lannister)):
    print("OK")
else:
    print("Something seems fishy, look at the code to see if \
the class king is inherited from the previous exercises")
