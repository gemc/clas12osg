# Database class definition
#
import os.path

# dbname can be a server address (MYSQL) or a filename (SQLITE)
# version can be production or devel

class Database():

	# constructor from Steering Card (scard) text file
	def __init__(self, dbname, version):

		self.dbname         = dbname
		self.version        = version



	def connect_to_mysql(host, username, password, db_name):

		# This is so tests work on travis-ci, where we ue root user
		if username == 'root':
			host='localhost'

		return MySQLdb.connect(host, username, password, db_name)


#db = Database()
#print(conf.client_ip)
