import subprocess
from random import randint
import sys

from discord.ext.commands import command
from .cog import Cog

def codify(*lines, language=""):
    return ''.join(f'```{language}\n'+line+'```\n' for line in lines)

class CLI(Cog):
    @command()
    async def cli(self, code, *m):
        """Run commands from my command line. Plz don't. Requires code anyways."""
        if self.bot.check_code(code):
            p = subprocess.run(args=m, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            await self.bot.reply(codify(p.stdout.decode('utf-8'), p.stderr.decode('utf-8')))
        else:
            await self.bot.reply('Bad code!')

    @command()
    async def check(self, code):
        """Checks to see if the code is good. If True the code resets."""
        await self.bot.reply(self.bot.check_code(code))

def setup(bot):
    bot.add_cog(CLI(bot))
