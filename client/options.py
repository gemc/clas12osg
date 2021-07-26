# Import packageds/modules
import argparse

# This function will return all command line arguemnts as an object
def get_args():

	# Initalize an argparser object. Documentation on the argparser module is here:
	# https://docs.python.org/3/library/argparse.html
	argparser = argparse.ArgumentParser(prog='Submit', usage='%(prog)s [options]')

	# adding argument nargs='+' would make this option an array
	argparser.add_argument('scardFile', metavar='scard', type=str,  help='Steering card text file')

	# Add ability for user to specify that they want to use SQLite, instead of MySQL database
	# Also, lets user specify the name and path of the SQLite DB file to use
	argparser.add_argument('--sqlite', help="use SQLITE file as DB", type=str, default=None)
  
	# Boolean arguement of using TEST MySQL DB or the main MySQL DB
	argparser.add_argument('--test', action='store_true', help='Use table CLAS12TEST instead of default CLAS12OCR', default=False)
  
	# Convert the arguement strings into attributes of the namespace
	args = argparser.parse_args()

	return args
