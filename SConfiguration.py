# SConfiguration class definition
#
import os.path

# version can be PRODUCTION or TEST

class SConfiguration():

	# constructor from Steering Card (scard) text file
	def __init__(self, scardFile):

		self.file           = None
		self.content        = None
		self.type           = None
		self.version        = None
		self.username       = None
		self.project        = None
		self.configuration  = None
		self.generator      = None
		self.genOptions     = None
		self.nevents        = None
		self.jobs           = None
		self.client_ip      = None
		self.fields         = None
		self.torus          = None
		self.solenoid       = None
		self.bkmerging      = None

		# open txt file, read and fill:
		if os.path.isfile(scardFile):
			# get scard content
			self.file = scardFile
			with open(scardFile) as openedFile:
				# stripping white spaces
				self.scardContent="".join(line.replace(" ", "") for line in openedFile)
				self.parseSCard(self.scardContent)
		else:
			sys.exit('Fatal error: {0} not found'.format(self.file))


	# scardContent is
	def parseSCard(self, scardContent):
		print('Parsing {0} content'.format(self.file));

		# splitting content into lines, criteria is carriage return
		scard_lines = scardContent.split("\n")
		for line in scard_lines:
			if not line:
				print('File {0} parsed successfully'.format(self.file))
				break
			pos_delimeter_colon = line.find(":")
			key   =  line[:pos_delimeter_colon].strip()
			value =  line[pos_delimeter_colon+1:].strip()

			# only set attributes that exist
			if hasattr(self, key) and not 'file' in key:
				setattr(self, key, value)
			else:
				sys.exit('Fatal error: key {0} not found in scard content'.format(key))

#	def from_database(mysqlDatabase) -> 'GConfiguration':


#conf = SConfiguration('test.txt')
#print(conf.client_ip)

