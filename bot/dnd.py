from random import randint, choice

from discord.ext.commands import command
from discord import Member
from names import get_full_name
from pony.orm import db_session

from .cog import Cog
from .dicebag import Character, Race, Role

class DnD(Cog):
    @command()
    async def rand(self, min: int=1, max: int=20):
        """Gets a random number."""
        await self.bot.reply(randint(min, max))

    @command()
    async def chars(self):
        with db_session:
            c = ', '.join(str(char) for char in Character.select())
            await self.bot.reply(c)

    @command()
    async def choose(self, *choices):
        """Pick between some options."""
        if not choices:
            await self.bot.reply('I need options bud.')
        else:
            await self.bot.reply(choice(choices))

    @command()
    async def name(self, gender=None):
        """Gets a random fairly normal name. Pick a gender use male/female."""
        await self.bot.reply(get_full_name(gender=gender))

def setup(bot):
    bot.add_cog(DnD(bot))
