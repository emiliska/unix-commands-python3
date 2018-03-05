import sys, os

# How to use:
# python .\mvPython.py '.\mvPython.py' 'D:\USERNAME\DESTINATION_FOLDER...'

for arg in sys.argv[1:]: # loop through arguments from command line
	os.remove(arg)

