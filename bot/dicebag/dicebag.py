from pony.orm import db_session
from .models import Race, Role, Character

with db_session:
    for race in ['Human', 'Dwarf', 'Elf', 'Halfling']:
        Race(name=race)

    for role in ['Warrior', 'Magic-User', 'Thief', 'Cleric']:
        Role(name=role)
