print('''----------------------------------------------
List issued Books
-------------------------
================================================================================
Callno      Book Name          Student ID     Students Name       Return Date
================================================================================''')
file = open("listissuebook.txt", "r")
for line in file:
  #Let's split the line into an array called "fields" using the "," as a separator:
  fields = line.split(",")
  #and let's extract the data:
  callno = fields[0]
  sid = fields[1]
  sname = fields[2]
  rdate = fields[3]
  #Print the books
  print(callno + " \t " + sid + " \t " + sname+ " \t\t " + rdate)
callno=input('Enter book callno: ')
sid=input('Enter student ID: ')
sname=input('Enter student name: ')
rdate=input('Enter return date: ')
f.close()
