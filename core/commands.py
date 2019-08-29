import discord
from discord.ext import commands

class Commands(cogs.Command):
	def __init__(self, bot):
		pass


def setup(bot):
	bot.add_cog(Commands(bot))