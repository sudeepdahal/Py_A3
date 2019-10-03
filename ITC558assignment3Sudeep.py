import time
availableBooks = dict()
issuedBooks = dict()
def main():
	menuNo = getMainMenuNo()
	# After getting Validated menu no the flow goes accordingly
	if menuNo == 1 : addBook();main()
	if menuNo == 2 : listAvailableBooks();main()
	if menuNo == 3 : issueBook();main()
	if menuNo == 4 : listIssuedBook();main()
	if menuNo == 5 : returnIssueBook();main()
	if menuNo == 6 : exitProgram()
def addBook():
	nextEntry = 'y'
	while nextEntry.lower() == 'y':
		# Opening a book.txt file in append mode
		f = open("book.txt", "a")
		print('---------------\nAdd Book Form\n---------------')
		# Input and Check for existing call no function call
		callno=getCallNo()
		bookName=input('Enter book name: ')
		author=input('Enter author name: ')
		pyear=input('Enter publish year: ')
		quantity=input('Enter book quantity: ')
		# Validating for integer quantity
		while not quantity.isdigit():
		    quantity = input("Invalid input \nEnter book quantity:")
		# Writing in a file
		f.write(str(callno)+','+bookName+','+author+','+pyear+','+quantity+'\n')
		# Closing file after adding entry
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
		global availableBooks
		availableBooks = dict()
		# To update the added record to the dictionary
		availableBooks = getAvailableBooksFromFile()
		while True:
			nextEntry=input('Do you want to enter details for another book (Y/N)?')
			if nextEntry.lower() == 'n' or nextEntry.lower() == 'y': break
			else: continue
def getCallNo():
	# Opening file in read mode to read the existing callno
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
			print("Invalid input.Please Input integer only ")
			continue
		else:
			if (str(callno) in callnoset):
				print("Please enter unique callno it exist in database")
				continue
			else:
				return callno
				break
def listAvailableBooks():
  if len(availableBooks) > 0:
    print('''
----------------------------------------------
List Available Books
-------------------------
=========================================================================
Callno      Name              Author            Publish Year    Quantity
=========================================================================''')
    for key,val in availableBooks.items():
      #Print the books
      print('{:10} {} {:>13} {:>13} {:>13}'.format(key, val[0], val[1], val[2], val[3]))
  else:
    print('There is no available Books')
def issueBook():
	nextEntry = 'y'
	while nextEntry.lower() == 'y':
		global issuedBooks
		global availableBooks
		# print(availableBooks)
		print('''
----------------------------------------------
Issue Book
--------------------------''')
		if len(availableBooks) > 0:
			callno=input('Enter book callno: ')
			while (callno not in availableBooks):
				callno = input('Sorry Call number doesnot exists\nEnter valid book callno: ')
			
			sid=input('Enter student ID: ')
			sname=input('Enter student name: ')
			rdate=input('Enter return date: ')
			setOfBooks = availableBooks[callno]
			#Decremenent of book quantity by 1
			setOfBooks[3] = setOfBooks[3]-1
			availableBooks[callno] = setOfBooks
			bookName=setOfBooks[0]
			ts = time.time()
			# Adding Issue Book in list with the timestamp of dictionary key
			issuedBooks[ts] = [callno,bookName,sid,sname,rdate]
			while True:
				nextEntry=input('Do you want to issue another book (Y/N)?')
				if nextEntry.lower() == 'n' or nextEntry.lower() == 'y': break
				else: continue
		else:
			print('No available Books to issue')
			break
def listIssuedBook():
	print('''
----------------------------------------------
List issued Books
-------------------------
================================================================================
Callno      Book Name          Student ID     Students Name       Return Date
================================================================================''')
	if len(issuedBooks) == 0:
		print('No issued book till now')
	else:
		for key,val in issuedBooks.items():
			#Print the book details
			print('{:10} {} {:>9} {:>18} {:>21}'.format(val[0], val[1], val[2], val[3], val[4]))
def returnIssueBook():
	nextEntry = 'y'
	while nextEntry.lower() == 'y':
		print('''
-----------------------
Return Book
-----------------------''')
		didNotIssued = True
		global issuedBooks
		global availableBooks
		if len(issuedBooks)>0:
			callno = input('Enter book callno: ')
			sid=input('Enter student ID: ')
			for key,val in issuedBooks.items():
				if (callno == val[0] and sid == val[2]):
					#remove from issued book dictionary
					issuedBooks.pop(key)
					returnBooks = availableBooks[callno]
					#Increase of book quantity by 1 in the available book dictionary
					returnBooks[3] = returnBooks[3]+1
					availableBooks[callno] = returnBooks
					print('Book returned successfully')
					didNotIssued = False
					break
			if didNotIssued : print('The student has not taken this book callno: ')
		else:
			print('No Books to return')
		while True:
			nextEntry=input('Do you want to enter details for another book (Y/N)?')
			if nextEntry.lower() == 'n' or nextEntry.lower() == 'y': break
			else: continue
def getAvailableBooksFromFile():
  availableBooks = dict()
  #If file is not present it will open file in append mode
  file = open("book.txt", "a")
  file.close()
  # Opening a file in read mode
  file = open("book.txt", "r")
  for line in file:
    #Let's split the line into an array called "fields" using the "," as a separator:
    fields = line.split(",")
    #and let's extract the data:
    callno = fields[0]
    bookName = fields[1]
    author = fields[2]
    pyear = fields[3]
    quantity = int(fields[4])
    if (quantity >=1):
    #Each key in the dictionary is a book callno
    #  Python list contains book information (Book Name, Author, Publish year, Quantity).
      availableBooks[callno] = [bookName,author,pyear,quantity]
  # Closeing the file
  file.close()
  return availableBooks
def exitProgram():
	print('Thanks for using the library management software\nSee you again!')
	exit()

def getMainMenuNo():
	print('''
=================================
LIBRARY MANAGEMENT SOFTWARE           
		MAIN MENU 
==================================
<1> Add book
<2> List Available Books
<3> Issue Book
<4> List Issued Books
<5> Return Book
<6> Exit
===================================''')
	menuNo = None
	#Validating to get positive int value from 1 to 6
	while True:
		try:
			menuNo = int(input('\nPlease input the menu Number: '))
		except ValueError:
			print("Invalid input.Please Input Number from 1 to 6")
			continue
		else:
			if (menuNo<=0 or menuNo>=7):
				print("Invalid input.Please Input Number from 1 to 6")
				continue
			else:
				return menuNo
				break

availableBooks = getAvailableBooksFromFile()
main()
