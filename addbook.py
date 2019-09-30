def addBook():
	nextEntry = 'y'
	while nextEntry.lower() == 'y':
		# Opening a book.txt file in append mode
		f = open("book.txt", "a")
		print('---------------\nAdd Book Form\n---------------')
		callno=getCallNo()
		bookName=input('Enter book name: ')
		author=input('Enter author name: ')
		pyear=input('Enter publish year: ')
		quantity=input('Enter book quantity: ')
		f.write(str(callno)+','+bookName+','+author+','+pyear+','+quantity+'\n')
		f.close()
		successMessage=('''The details of the book you entered are as follows:
		Book callno: {callno}
		Book name: {bookName}
		Author name: {author}
		Enter publish year: {pyear}
		Quantity: {quantity}
		The record has been successfully added to the books.txt file.''')
		#printing the saved record message
		print(successMessage.format(callno=callno,bookName=bookName,author=author,pyear=pyear,quantity=quantity))
		nextEntry=input('Do you want to enter details for another book (Y/N)?')
def getCallNo():
	file = open("book.txt", "r")
	callnoset = set()
	for line in file:
		#Let's split the line into an array called "fields" using the "," as a separator:
		fields = line.split(",")
		#and let's add callno in the set which is feilds[0]:
		callnoset.add(fields[0])
	# Closing the file
	file.close()
	callno = None
	#Validating if input callno is int and does not exist in file
	while True:
		try:
			callno = int(input('\nEnter book callno: '))
		except ValueError:
			print("Invalid input.Please Input Number Call No. ")
			continue
		else:
			if (str(callno) in callnoset):
				print("Please enter unique callno it exist in database")
				continue
			else:
				return callno
				break