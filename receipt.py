# Imports
import os
from functions import *

# Input file name
file_name = input("Enter file name (enter 'done' to end): ")
while not file_name == "done":
	# Read/create files
	path_in = os.getcwd() + "\\HTMLs\\" + file_name + ".html"
	path_out = os.getcwd() + "\\CSVs\\" + file_name + ".csv"
	
	if (os.path.exists(path_in)):
		file_in = open(path_in, "r")
		file_out = open(path_out, "w")
		
		# Writing to file_out
		date, store, money = tangerineReader(file_in)
		tangerineWriter(date, store, money, file_out)

		# Close files
		file_in.close()
		file_out.close()
	else:
		print("File does not exist.")
	file_name = input("Enter file name (enter 'done' to end): ")
	




