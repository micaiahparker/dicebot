import os

from discord.ext.commands import Bot, when_mentioned_or
from discord.ext.commands import Command

bot = Bot(
    command_prefix=when_mentioned_or('?'),
    description="A real cool bot that doesn't do much of anything."
)

@bot.command()
async def bad():
    """Used to make me feel bad"""
    await bot.reply('sorry')

@bot.command()
async def good():
    """Used to make me feel good"""
    await bot.reply('thx')

@bot.command()
async def restart():
    """Restarts the bot"""
    await bot.reply('Restarting...')
    os.system('python -m bot')
    sys.exit()

@bot.event
async def on_ready():
    print("I'm up.")
