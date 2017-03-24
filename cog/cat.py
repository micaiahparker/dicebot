from discord.ext.commands import command
from io import BytesIO
import aiohttp

from .cog import Cog

class HttpCat(Cog):
    @command()
    async def code(self, status_code):
        """Cat HTTP errors, frick with iiit"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'http://http.cat/{status_code.strip()}.jpg') as r:
                await self.bot.upload(BytesIO(await r.read()), filename=f'{status_code}.jpg')

def setup(bot):
    bot.add_cog(HttpCat(bot))
