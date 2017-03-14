from random import randint, choice

from discord.ext.commands import command, group
from names import get_full_name
from pony.orm import db_session, sql_debug

from .cog import Cog
from .dicebag import Character, Race, Role

class DND(Cog):
    @command()
    async def characters(self):
        """Lists all of the created characters."""
        with db_session:
            characters = ', '.join(str(c) for c in Character.select())
            await self.bot.reply(characters)

    @group(pass_context=True)
    async def make(self, ctx):
        if not ctx.invoked_subcommand:
            await self.bot.reply('Make what??!')

    @make.command()
    async def race(self, name=None):
        """adds a new race"""
        if not name:
            await self.bot.reply("Needs a name")
            return None

        with db_session:
            r = Race(name=name.title())
            await self.bot.reply("Made: {}".format(r))

    @make.command()
    async def role(self, name=None):
        """adds a new role, should be class but.. python keyword"""
        if not name:
            await self.bot.reply('Needs a name')
            return None

        with db_session:
            r = Role(name=name.title())
            await self.bot.reply('Made: {}'.format(r))

    @make.command()
    async def character(self, race, role, name=None):
        """creates a new character"""
        name = name or get_full_name()

        with db_session:
            race = Race.get(name=race.title())
            role = Role.get(name=role.title())
            if race and role:
                await self.bot.reply(Character(name=name.title(), race=race, role=role))
            else:
                await self.bot.reply("Couldn't make character with race: {} or role: {}".format(race, role))


    @group(pass_context=True)
    async def ls(self, ctx):
        """Lists stuff"""
        if not ctx.invoked_subcommand:
            await self.bot.reply('list what??')

    @ls.command()
    async def races(self):
        with db_session:
            await self.bot.reply(', '.join(str(r) for r in Race.select()))

    @ls.command()
    async def roles(self):
        with db_session:
            await self.bot.reply(', '.join(str(r) for r in Role.select()))

    @ls.command()
    async def characters(self):
        with db_session:
            await self.bot.reply(', '.join(str(c) for c in Character.select()))


def setup(bot):
    sql_debug(bot.config.get_sql_debug())
    bot.add_cog(DND(bot))
