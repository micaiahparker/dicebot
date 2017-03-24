from discord.ext.commands import command
from discord.utils import snowflake_time
from pony.orm import db_session

from .cog import Cog
from .models import Swear, Swearer

def get_swears():
    return ['fuck', 'shit', 'piss', 'cunt', 'dick', 'damn', 'bitch']

class Nanny(Cog):
    @command()
    async def lswear(self, user=None):
        """basically just tattles"""
        if not user:
            with db_session:
                resp = ''
                swearers = Swearer.select().order_by(lambda x: x.count)
                if swearers:
                    for s in swearers:
                        resp += f'`{s}: {s.count}`\n'
                else:
                    resp = '`Yall good boyz \'n gurlz`'
                await self.bot.say(resp)

        if user:
            with db_session:
                swearer = Swearer.get(name=user)
                if swearer:
                    resp = ''
                    for swear in swearer.swears:
                        resp += f'`{swear}`\n'
                    await self.bot.say(resp)
                else:
                    await self.bot.say(f'{user}: `idk them`')


    async def on_message(self, message):
        if not message.author.bot:
            n_swears = sum(int(word in message.content.lower()) for word in get_swears())
            if n_swears:
                with db_session:
                    user = Swearer.get(user_id=message.author.id)
                    if not user:
                        user = Swearer(user_id=message.author.id, name=message.author.name, nick=message.author.nick)
                    swear = Swear(msg_id=message.id, swear=str(message.content), author=user)
                    user.swear(n_swears)
                    await self.bot.add_reaction(message, u"\u203C")

def setup(bot):
    bot.add_cog(Nanny(bot))
