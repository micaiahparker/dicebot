from .bot import bot

for extension in bot.config.get_extensions():
    try:
        bot.load_extension(extension)
        print('Added: {}'.format(extension))
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(bot.config.get_key())
