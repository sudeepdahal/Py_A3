import listbook
import time
# def main():
issuedBooks = dict()
availableBooks = listbook.listBook(3)
def issueBook():
	nextEntry = 'y'
	while nextEntry.lower() == 'y':
		print(availableBooks)
		print('''
----------------------------------------------
Issue Book
--------------------------''')
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
		ts = time.time()
		issuedBooks[ts] = [callno,sid,sname,rdate]

		print(availableBooks)
		print(issuedBooks)
		nextEntry=input('Do you want to issue another book (Y/N)?')
# main()
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
		# print(issuedBooks)
		for key,val in issuedBooks.items():
		  #Print the book details
		  print( val[0] , " \t " , val[1], " \t\t " , val[2], " \t\t " , val[3])

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
				if (callno == val[0] and sid == val[1]):
					#remove from issued book dictionary
					issuedBooks.pop(key)
					returnBooks = availableBooks[callno]
					#Increase of book quantity by 1 in the available book dictionary
					returnBooks[3] = returnBooks[3]+1
					availableBooks[callno] = returnBooks
					# print(issuedBooks)
					print('Book returned successfully')
					didNotIssued = False
					break
			if didNotIssued : print('The student has not taken this book callno: ')
		else:
			print('No Books to return')
		nextEntry=input('Do you want to return another book (Y/N)? ')

		