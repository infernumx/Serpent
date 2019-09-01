import discord
from discord.ext import commands
from tools import extensions

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
	print('Bot initialized.')

exts = [
	'core.commands'
]

for ext in exts:
	try:
		bot.load_extension(ext)
	except Exception as e:
		print('{}: {}'.format(type(e).__name__, e))

config = extensions.load_json('config.json')
bot.run(config['bot']['token'])
