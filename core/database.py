import pymysql.cursors

class DatabaseConnection:
	def __init__(self, credentials):
		self.connection = pymysql.connect(**credentials)
		self.auto_setup()

	def auto_setup(self):
		schema = """
		CREATE TABLE IF NOT EXISTS `bot_listener` (
		    `id` int(6) PRIMARY KEY AUTO_INCREMENT,
		    `command` VARCHAR(255),
		    `arguments` VARCHAR(2000)
		);
		CREATE TABLE IF NOT EXISTS `server_listener` (
		    `id` int(6) PRIMARY KEY AUTO_INCREMENT,
		    `command` VARCHAR(255),
		    `arguments` VARCHAR(2000)
		);
		"""

		self.query(schema)

	def query(self, q):
		try:
			with self.connection.cursor() as cursor:
				cursor.execute(q)
				self.connection.commit()
		except Exception as e:
			print('{}: {}'.format(type(e).__name__, e))
		else:
			return cursor.fetchall()