import pymysql.cursors

class DatabaseConnection:
	def __init__(self, credentials):
		print('Creating database connection to "{}": {}@{}'.format(credentials['db'], credentials['user'], credentials['bind_address']))
		self.connection = pymysql.connect(**credentials)
		
		if not self.query("""SHOW TABLES LIKE 'bot_listener'"""):
			self.first_time_setup()

	def first_time_setup(self):
		print('Performing first time setup...')
		self.query("""CREATE TABLE IF NOT EXISTS `bot_listener` (
		    `id` int(6) PRIMARY KEY AUTO_INCREMENT,
		    `command` VARCHAR(255),
		    `arguments` VARCHAR(2000)
		);""")
		self.query("""CREATE TABLE IF NOT EXISTS `server_listener` (
		    `id` int(6) PRIMARY KEY AUTO_INCREMENT,
		    `command` VARCHAR(255),
		    `arguments` VARCHAR(2000)
		);""")
		print('Done.')

	def query(self, q):
		try:
			with self.connection.cursor() as cursor:
				cursor.execute(q)
				self.connection.commit()
		except Exception as e:
			print('{}: {}'.format(type(e).__name__, e))
		else:
			return cursor.fetchall()