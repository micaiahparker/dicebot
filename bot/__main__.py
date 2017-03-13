from .bot import bot
from .config import Config

config = Config()

for extension in config.get_extensions():
    try:
        bot.load_extension(extension)
        print('Added: {}'.format(extension))
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.get_key())
