import discord
from discord.ext import commands
from core.database import DatabaseConnection

class Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def test(self, ctx):
		print(ctx.message)


def setup(bot):
	bot.add_cog(Commands(bot))