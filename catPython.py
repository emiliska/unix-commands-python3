import sys

pretty = "*****"

if len(sys.argv) < 2:
	print(pretty + 'catPython.py HELP' + pretty
	+ "\n Hm.. It seems you aren't using this python script quite right." 
	+ '\n Maybe this example will help:'
	+ '\n python catPython.py <filename> ...\n'
	+ pretty + "*****************" + pretty)	

else:
	for arg in sys.argv[1:]: # loop through arguments from command line
		with open (arg) as file: # open file
			# set contents of file equal to var contents
			contents = file.read() 
			print(contents)
		
