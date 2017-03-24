import os

class Config:
    def __init__(self):
        self.BOT_KEY = os.environ.get('BOT_KEY')
        self.startup_extensions = ['cog.dnd', 'cog.cli', 'cog.rng', 'cog.tic', 'cog.cat', 'cog.nanny']
        self.SQL_DEBUG = bool(os.environ.get('SQL_DEBUG', False))

    def get_key(self):
        return self.BOT_KEY

    def get_extensions(self):
        return self.startup_extensions

    def get_sql_debug(self):
        return self.SQL_DEBUG
