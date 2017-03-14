import os
import sys
import asyncio
from random import randint
from discord.ext.commands import command, when_mentioned_or

from .dicebot import Dicebot

bot = Dicebot(
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
async def fix():
    """Hehehe"""
    msg = await bot.reply("ben is best")
    await asyncio.sleep(3)
    await bot.edit_message(msg, msg.content.replace('ben', 'micaiah'))

@bot.command()
async def restart():
    """Restarts the bot"""
    await bot.reply('Restarting...')
    bot.restart()

@bot.event
async def on_ready():
    print("New code:", bot.get_code())
    print("I'm up.")
