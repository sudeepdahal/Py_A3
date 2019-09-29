# cn0 = 'child1'
# child1 = {
#     "name" : "Emil",
#     "year" : 2004 }
# myfamily = {
#     cn0 : child1
#   ,
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)
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
		availableBooks[callno] = [bookName,author,pyear,quantity]
for key,val in availableBooks.items():
  print(key , " \t " , val[0] , " \t " , val[1], " \t\t " , val[2], " \t\t " , val[3])
  # print(key,val[3])
# print(availableBooks)