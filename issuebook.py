print('''----------------------------------------------
     Issue Book
--------------------------''')
callno=input('Enter book callno: ')
sid=input('Enter student ID: ')
sname=input('Enter student name: ')
rdate=input('Enter return date: ')
f = open("issuedBook.txt", "a")
f.write(callno+','+sid+','+sname+','+rdate+'\n')
print('Book issued successfully')
issueNext=input('Do you want to issue another book (Y/N)? ')
f.close()
f = open("issuedBook.txt", "r")
print(f.read())
f.close()