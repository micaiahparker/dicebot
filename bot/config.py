import os

class Config:
    def __init__(self):
        self.BOT_KEY = os.environ.get('BOT_KEY')
        self.startup_extensions = ['bot.dnd']

    def get_key(self):
        return self.BOT_KEY

    def get_extensions(self):
        return self.startup_extensions
