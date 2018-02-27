import sys

for arg in sys.argv: # loop through arguments from command line
	with open (arg) as file: # open file
		contents = file.read() # set contents of file equal to var contents
	with open (sys.argv[1], 'w') as file:
		file.write(contents)	
		
