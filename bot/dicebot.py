import os
import sys

from random import randint
from discord.ext.commands import Bot

class Dicebot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = self.gen_code()

    def get_code(self):
        return self.code

    def gen_code(self, n=5):
        return ''.join(str(randint(0, 9)) for _ in range(n))

    def check_code(self, code):
        if self.code == code:
            self.code = self.gen_code()
            print("New Code:", self.code)
            return True
        return False

    async def die(self):
        await self.logout()
        self.loop.stop()
        sys.exit()

    async def restart(self):
        await self.logout()
        self.loop.stop()
        os.system('python -m bot')
        sys.exit()
