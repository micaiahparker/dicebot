import subprocess
from random import randint
import sys
import asyncio

from discord.ext.commands import command
from .cog import Cog

def codify(*lines, language=""):
    return ''.join(f'```{language}\n'+line+'```\n' for line in lines if line)

class CLI(Cog):
    @command()
    async def cli(self, code, *m):
        """Run commands from my command line. Plz don't. Requires code anyways."""
        if self.bot.check_code(code):
            p = subprocess.run(args=m, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            await self.bot.say(codify(p.stdout.decode('utf-8'), p.stderr.decode('utf-8'), language='DOS'))
        else:
            await self.bot.reply('Bad code!')

    @command()
    async def check(self, code):
        """Checks to see if the code is good. If True the code resets."""
        await self.bot.reply(self.bot.check_code(code))

    @command()
    async def kill(self, code=''):
        """RIP"""
        if self.bot.check_code(code):
            await self.bot.reply('goodbye cruel world')
            await self.bot.die()
        else:
            await self.bot.reply('what is ded will nvr die')

    @command()
    async def print_code(self):
        """Prints out the code, because sometimes I don't feel like scrolling for it."""
        print("Current code:", self.bot.get_code())
        await self.bot.reply('k')

    @command()
    async def remind(self, s:int, message="Remind me!"):
        """Sets a reminder in seconds"""
        await asyncio.sleep(int(s))
        await self.bot.reply("Reminder: {}".format(message))

def setup(bot):
    bot.add_cog(CLI(bot))
