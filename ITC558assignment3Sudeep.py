import addbook 
import listbook
import issuebook
def main():
	menuNo = mainMenu()
	print (menuNo)
	if menuNo == 1 : addbook.addBook();main()
	if menuNo == 2 : listbook.listBook(menuNo);main()
	if menuNo == 3 : issuebook.issueBook();main()
	if menuNo == 4 : issuebook.listIssuedBook();main()
	if menuNo == 5 : issuebook.returnIssueBook();main()
	if menuNo == 6 : exitProgram()

def addBook():
	print('pass')
def exitProgram():
	print('Thanks for using the library management software\nSee you again!')
	exit()

def mainMenu():
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

				# user_number  = input("Enter your number")
				# while not user_number.isdigit():
				#     user_number  = input("Invalid ip \nEnter your number")
				# print(user_number)

main()
