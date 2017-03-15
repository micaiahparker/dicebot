from pony.orm import *


db = Database()

class Race(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    characters = Set('Character')

    def __str__(self):
        return self.name

class Role(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    characters = Set('Character')

    def __str__(self):
        return self.name

class Character(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    race = Required(Race)
    role = Required(Role)

    def __str__(self):
        return self.name

db.bind("sqlite", "dicebag.db", create_db=True)
db.generate_mapping(create_tables=True)
