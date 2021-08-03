# SConfiguration class definition
#
import os.path
import sys


class SConfiguration():

	# constructor from Steering Card (scard) text file
	def __init__(self, scardFile):

		self.file           = None   # steering card file
		self.content        = None   # full content of steering card
		self.project        = None   # OSG project
		self.type           = None   # submission type: 1 or 2
		self.connection     = None   # connection: mysql or sqlite
		self.version        = None   # portal version (production or devel)
		self.username       = None   # username
		self.configuration  = None   # configuration: rga, rgb, etc
		self.generator      = None   # generator name for type 1, or address for type2
		self.genOptions     = None
		self.nevents        = None
		self.njobs          = None
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

	def show(self):
		print('SConfiguration:');
		print('- file:          {0}'.format(self.file));
		print('- project:       {0}'.format(self.project));
		print('- type:          {0}'.format(self.type));
		print('- connection:    {0}'.format(self.connection));
		print('- version:       {0}'.format(self.version));
		print('- username:      {0}'.format(self.username));
		print('- configuration: {0}'.format(self.configuration));
		print('- generator:     {0}'.format(self.generator));
		print('- genOptions:    {0}'.format(self.genOptions));
		print('- nevents:       {0}'.format(self.nevents));
		print('- njobs:         {0}'.format(self.njobs));
		print('- client_ip:     {0}'.format(self.client_ip));
		print('- torus:         {0}'.format(self.torus));
		print('- solenoid:      {0}'.format(self.solenoid));
		print('- bkmerging:     {0}'.format(self.bkmerging));


# running this as stand-alone:
# python SConfiguration.py
#conf = SConfiguration('test/t1test1.txt')
#conf.show()
