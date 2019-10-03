import listbook
import time
# def main():

issuedBooks = {1570062577.2741902: ['1', 'c programming', '12', 'sudeep', '2/11/2019'], 1570062626.3554623: ['2', 'c++ programming', '13', 'rambabu', '4/12/2019']}
# {1570062577.2741902: ['1', 'c programming', '12', 'sudeep', '2/11/2019']}
# dict()
availableBooks = listbook.getAvailableBooks()
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
		# Adding Issue Book in list with the timestamp of dictionary key
		issuedBooks[ts] = [callno,sid,sname,rdate]

		# print(availableBooks)
		# print(issuedBooks)
		nextEntry=input('Do you want to issue another book (Y/N)?')
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
		# print('here')
		# print(issuedBooks)
		for key,val in issuedBooks.items():
			print('{:10} {} {:>9} {:>18} {:>21}'.format(val[0], val[1], val[2], val[3], val[4]))
			# print( val[0] , " \t " , val[1], " \t\t " , val[2], " \t\t " , val[3])


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

listIssuedBook()
returnIssueBook()