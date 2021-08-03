# Import packageds/modules
import argparse

# This function will return all command line arguemnts as an object
def get_args():

	# Initalize an argparser object. Documentation on the argparser module is here:
	# https://docs.python.org/3/library/argparse.html
	argparser = argparse.ArgumentParser(prog='Submit', usage='%(prog)s [options]')

	# adding argument nargs='+' would make this option an array
	argparser.add_argument('scardFile', metavar='scard', type=str,  help='Steering card text file')

	# Convert the arguement strings into attributes of the namespace
	args = argparser.parse_args()

	return args
