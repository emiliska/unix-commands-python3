import sys

for arg in sys.argv[1:]: # loop through arguments from command line
	with open (arg) as file: # open file
		contents = file.read() # set contents of file equal to var contents
		print(contents)
		
