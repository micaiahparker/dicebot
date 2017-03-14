import os
import sys
import asyncio

from random import randint

from discord.ext.commands import Bot, when_mentioned_or
from discord.ext.commands import Command

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

    def restart(self):
        os.system('python -m bot')
        sys.exit()

bot = Dicebot(
    command_prefix=when_mentioned_or('?'),
    description="A real cool bot that doesn't do much of anything."
)


@bot.command()
async def bad():
    """Used to make me feel bad"""
    await bot.reply('sorry')

@bot.command()
async def good():
    """Used to make me feel good"""
    await bot.reply('thx')

@bot.command()
async def fix():
    """Hehehe"""
    msg = await bot.reply("ben is best")
    await asyncio.sleep(3)
    await bot.edit_message(msg, msg.content.replace('ben', 'micaiah'))

@bot.command()
async def restart():
    """Restarts the bot"""
    await bot.reply('Restarting...')
    bot.restart()

@bot.event
async def on_ready():
    print("New code:", bot.get_code())
    print("I'm up.")
