import sys, os

for arg in sys.argv[1:]: # loop through arguments from command line
	os.remove(arg)

