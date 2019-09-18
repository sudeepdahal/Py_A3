f = open("book.txt", "a")
print('---------------\nAdd Book Form\n---------------')
callno=input('Enter book callno: ')
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
f = open("book.txt", "r")
print(f.read())
