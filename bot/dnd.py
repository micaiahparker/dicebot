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
        await self.bot.reply(choice(choices))

def setup(bot):
    bot.add_cog(DnD(bot))
