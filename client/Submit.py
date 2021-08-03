#!/usr/bin/env python

# adding one dir up to path
import sys
sys.path.append("..")
sys.path.append(".")
sys.path.append("database")

import options
from SConfiguration import SConfiguration
from Database import Database

# get command line arguments, log to screen
args = options.get_args()
print(args)


# build SConfiguration from Steering Card (SCard) text file
submitConfiguration = SConfiguration(args.scardFile)
submitConfiguration.show()
