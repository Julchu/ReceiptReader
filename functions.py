def isUpper(line):
	"""
	Check if line consists entirely of capitals
	"""
	# Constants
	CAP = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	
	# Variables
	isUpper = False
	n = len(line)
	count = 0
	
	# Calculation
	for x in range(n):
		if line[x].isalpha():
			if line[x] in CAP:
				count += 1
	if (n > 3 and count > 3) or (n <= 3 and count > 1):
		isUpper = True
	# Return true if all characters are capital
	return isUpper
	
def isDate(line):
	"""
	Check if line is a date using format: NN-AAA
	"""
	# Variables
	isDate = False
	
	# Calculation
	if (line[0:2].isdigit()) and (line[2] == "-") and (line[3:6].isalpha()):
		isDate = True
	
	# Return true if string meets format
	return isDate
	
def isMoney(line):
	"""
	Checks if line is money
	"""
	# Variables
	isMoney = False
	
	# Calculation
	if (len(line) > 4):
		if (line[-3] == "."):
			line = line[:-3] + line[-3:]
			isMoney = True
		
	# Returns true if line is money, float value
	return isMoney
	
def replaceChar(line):
	"""
	Removes characters from line
	"""
	# Characters to be removed
	CHARS = ["<A name=2></a>", "<b>", "</b>", "<i>", "</i>", ",", "$", "("]
	
	# Calculation
	if "&amp;" in line:
			line = line.replace("&amp;", "&")
	for x in CHARS:
		line = line.replace(x, "")

	# Return string
	return line

def tangerineReader(file_in):
	# Initializing loops
	done = False
	start = False

	# Variables
	#oldBalance = 0
	#newBalance = 0
	date = []
	store = []
	money = []

	# Reading every line; array size is 2, array[1] holds empty string
	line = str(file_in.readline().strip().split("<br>")[0])

	# Finding start of transactions (find: "Previous Balance")
	while (line.find("Previous Balance") == (-1)):
		line = str(file_in.readline().strip().split("<br>")[0])

	# Storing previous balance
	oldBalance = replaceChar(str(file_in.readline().strip().split("<br>")[0]))
	# Sabrina doesn't need:
	#data += ",{},{}\n".format("Previous Balance", oldBalance)

	while not done:
		# Finding start of next transaction; transactions start with date
		while not isDate(line):
			# Checking if at end of transaction list (find: "New Balance")
			if (line.find("New Balance") != (-1)):
				newBalance = replaceChar(str(file_in.readline().strip().split("<br>")[0]))
				# Sabrina doesn't need:
				#data += ",{},{}".format("New Balance", newBalance)
				
				# End loops
				done = True
				start = True
				line = "99-AAA"
			else:
				line = str(file_in.readline().strip().split("<br>")[0])
				
		if not start:
			if (isDate(line)):
				d = replaceChar(line)
				date.append(d)
				
			# Finding next store
			while not (isUpper(line)):
				line = str(file_in.readline().strip().split("<br>")[0])

			if (isUpper(line)):
				s = replaceChar(line)
				store.append(s)
			
			# Finding next monetary value
			while not (isMoney(line)):
				line = str(file_in.readline().strip().split("<br>")[0])

			if (isMoney(line)):
				m = replaceChar(line)
				money.append(m)
	return date, store, money

def tangerineWriter(date, store, money, file_out):
	# Variables
	n = len(date) - 1
	s = ""
	
	for x in range(n, 0, -1):
		s += date[x][:-5] + ","
	s += "\n"
	
	for x in range(n, 0, -1):
		s += money[x] + ","
	s += "\n"
	
	for x in range(n, 0, -1):
		s += store[x] + ","
	
	file_out.write(s)
