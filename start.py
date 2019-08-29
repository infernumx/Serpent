import discord
from discord.ext import commands
import rapidjson as json

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
	print('Bot initialized.')

extensions = [
	'core.commands'
]

for ext in extensions:
	try:
		bot.load_extension(ext)
	except Exception as e:
		print('{}: {}'.format(type(e).__name__, e))

with open('config.json') as f:
	j = json.loads(f.read())
	bot.run(j['bot']['token'])

# Invite link: https://discordapp.com/oauth2/authorize?&client_id=616492312473632768&scope=bot&permissions=8