from pony.orm import *
import pendulum
from discord.utils import snowflake_time

db = Database()

class Swearer(db.Entity):
    user_id = Required(str)
    name = Required(str)
    nick = Optional(str, nullable=True)
    count = Required(int, default=0)
    swears = Set('Swear')

    @db_session
    def swear(self, n_swears=1):
        self.count += n_swears

    def __str__(self):
        return self.nick or self.name

class Swear(db.Entity):
    author = Required(Swearer)
    swear = Required(str)
    msg_id = Required(str)

    def __str__(self):
        return f'{self.author}: {self.swear} - {self.get_human_time()}'

    def get_human_time(self):
        return pendulum.parse(str(snowflake_time(self.msg_id))).diff_for_humans()

    def get_time(self):
        return pendulum.parse(str(snowflake_time(self.msg_id))).utc()

db.bind('sqlite', 'nanny.db', create_db=True)
db.generate_mapping(create_tables=True)
