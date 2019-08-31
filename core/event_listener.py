import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler

class EventListener(commands.Cog):
	def __init__(self, bot, db_conn):
		self.bot = bot
		self.db_conn = db_conn

	def start(self, interval):
		self.scheduler = AsyncIOScheduler()
		self.scheduler.add_task(self.exec_listener, 'interval', seconds=interval)
		self.scheduler.start()

	async def exec_listener(self):
		pass

	def get_event_queue(self):
		return self.db_conn.query("""SELECT * FROM `server_listener`""")