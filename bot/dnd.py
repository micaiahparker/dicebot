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
    async def role(self, role_name=None):
        """Lists info about roles"""
        with db_session:
            if role_name:
                await self.bot.reply(Role.get(name=role_name.title()))
            else:
                await self.bot.reply(' '.join(role.name for role in Role.select()))

    @command()
    async def race(self, race_name=None):
        """Lists info about races"""
        with db_session:
            if race_name:
                await self.bot.reply(Race.get(name=race_name.title()))
            else:
                await self.bot.reply(' '.join(race.name for race in race.select()))

    @command()
    async def make_character(self, race, role, name=None):
        with db_session:
            name = name or get_full_name()
            race, role = Race.get(name=race.title()), Role.get(name=role.title())
            if race and role:
                c = Character(race=race, role=role, name=name)
                await self.bot.reply('Made: {}'.format(c))
            else:
                await self.bot.reply(f'Failed to create person with race: {race} and role {role}')

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
