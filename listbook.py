def listBook(menuNo):
  availableBooks = dict()
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
  if menuNo == 2:
    print('''----------------------------------------------
    List Available Books
    -------------------------
    =========================================================================
    Callno      Name              Author            Publish Year    Quantity
    =========================================================================''')
    for key,val in availableBooks.items():
      #Print the books
      print(key , " \t " , val[0] , " \t " , val[1], " \t\t " , val[2], " \t\t " , val[3])
  else:
    return availableBooks
