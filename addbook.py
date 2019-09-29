thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
def addBook():
	nextEntry = 'y'
	while nextEntry.lower() == 'y':
		f = open("book.txt", "a")
		print('---------------\nAdd Book Form\n---------------')
		getAllCallNo=getCallNo()
		callno=input('Enter book callno: ')
		while (callno in getAllCallNo):
			callno = input('Please enter unique callno\nEnter book callno: ')
		bookName=input('Enter book name: ')
		author=input('Enter author name: ')
		pyear=input('Enter publish year: ')
		quantity=input('Enter book quantity: ')
		f.write(callno+','+bookName+','+author+','+pyear+','+quantity+'\n')
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
		# f = open("book.txt", "r")
		# print(f.read())
def getCallNo():
	file = open("book.txt", "r")
	callnoset = set()
	for line in file:
		#Let's split the line into an array called "fields" using the "," as a separator:
		fields = line.split(",")
		#and let's add callno in the set:
		callnoset.add(fields[0])
	return callnoset
def checkIfCallNoExists():
	pass
