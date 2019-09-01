import discord
from discord.ext import commands
from core.database import DatabaseConnection
from core.event_listener import EventListener
from tools import extensions

config = extensions.load_json('config.json')
db_conn = DatabaseConnection(config["database"])

class Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.event_listener = EventListener(bot, db_conn)

	def enqueue(self, command, args = ""):
		query = 'INSERT INTO `bot_listener` (`id`, `command`, `arguments`) VALUES (NULL, "{}", "{}")'.format(command, args)
		db_conn.query(query)

	@commands.command()
	async def online(self, ctx):
		self.enqueue('online')

	@commands.command()
	async def uptime(self, ctx):
		self.enqueue('uptime')

def setup(bot):
	bot.add_cog(Commands(bot))