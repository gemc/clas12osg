# Database class definition
#
import os.path

# type can be a server address (MYSQL) or a filename (SQLITE)
# version can be production or devel

class Database():

	# constructor from Steering Card (scard) text file
	def __init__(self, dbname, version):

		self.dbname         = dbname
		self.version        = version



#conf = Database('mysql')
#print(conf.client_ip)

