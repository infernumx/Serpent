import discord
from discord.ext import commands
from core.database import DatabaseConnection
import rapidjson

with open('config.json') as f:
	config = rapidjson.loads(f.read())
	database = DatabaseConnection(config.get("database"))

class Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def test(self, ctx):
		print(ctx.message)


def setup(bot):
	bot.add_cog(Commands(bot))