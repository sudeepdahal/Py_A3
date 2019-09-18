print('''----------------------------------------------
List Available Books
-------------------------
=========================================================================
Callno      Name              Author            Publish Year    Quantity
=========================================================================''')
file = open("book.txt", "r")
for line in file:
  
  #Let's split the line into an array called "fields" using the "," as a separator:
  fields = line.split(",")
  
  #and let's extract the data:
  callno = fields[0]
  bookName = fields[1]
  author = fields[2]
  pyear = fields[3]
  quantity = fields[4]
  
  #Print the books
  print(callno + " \t " + bookName + " \t " + author+ " \t\t " + pyear+ " \t\t " + quantity)
#print(f.read())
