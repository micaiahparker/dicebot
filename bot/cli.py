import subprocess
from random import randint
import sys

from discord.ext.commands import command
from .cog import Cog

class CLI(Cog):
    @command()
    async def hi(self):
        await self.bot.reply('hello')

    @command()
    async def cli(self, code, *m):
        """Run commands from my command line. Plz don't. Requires code anyways."""
        if self.bot.check_code(code):
            p = subprocess.run(args=m, stdout=subprocess.PIPE, shell=True)
            await self.bot.reply(p.stdout.decode('utf-8'))
        else:
            await self.bot.reply('bad code')

    @command()
    async def check(self, code):
        await self.bot.reply(self.bot.check_code(code))

def setup(bot):
    bot.add_cog(CLI(bot))
