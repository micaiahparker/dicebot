from discord.ext.commands import command
from names import get_full_name
from .cog import Cog

class RNG(Cog):
    @command()
    async def rand(self, min: int=1, max: int=20):
        """Gets a random number."""
        await self.bot.reply(randint(min, max))

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
    bot.add_cog(RNG(bot))
