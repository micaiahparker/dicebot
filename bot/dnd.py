from random import randint, choice

from discord.ext import commands
from discord import Member

from names import get_full_name

class DnD:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rand(self, min: int=1, max: int=20):
        """Gets a random number."""
        await self.bot.reply(randint(min, max))

    @commands.command()
    async def list_classes(self):
        """Lists available classes"""
        await self.bot.say("not yet")

    @commands.command()
    async def choose(self, *choices):
        """Pick between some options."""
        if not choices:
            await self.bot.reply('I need options bud.')
        else:
            await self.bot.reply(choice(choices))

    @commands.command()
    async def name(self, gender=None):
        """Gets a random fairly normal name. Pick a gender use male/female."""
        await self.bot.reply(get_full_name(gender=gender))

def setup(bot):
    bot.add_cog(DnD(bot))
