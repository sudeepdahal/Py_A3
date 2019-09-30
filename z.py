# def getCallNo():
# 	file = open("book.txt", "r")
# 	callnoset = set()
# 	for line in file:
# 		#Let's split the line into an array called "fields" using the "," as a separator:
# 		fields = line.split(",")
# 		#and let's add callno in the set:
# 		callnoset.add(fields[0])
# 	file.close()
# 	callno = None
# 	#Validating if input callno is int and does not exist in file
# 	while True:
# 		try:
# 			callno = int(input('\nEnter book callno: '))
# 		except ValueError:
# 			print("Invalid input.Please Input Number Call No. ")
# 			continue
# 			# finally:
# 		else:
# 			if (str(callno) in callnoset):
# 				print("Please enter unique callno it exist in database")
# 				continue
# 			else:
# 				return callno
# 				break
# def main():
# 	callno = getCallNo()
# 	print(callno)
# main()
user_number  = ' and callno > 0:'
# input("Enter your string")
while not user_number.isstr() or len(user_number) == 0:
	user_number = input("Invalid ip \nEnter your number")
user_number = int(user_number)
# print(type(user_number))
# availableBooks = dict()
# file = open("book.txt", "r")
# for line in file:
# 	#Let's split the line into an array called "fields" using the "," as a separator:
# 	fields = line.split(",")
# 	#and let's extract the data:
# 	callno = fields[0]
# 	bookName = fields[1]
# 	author = fields[2]
# 	pyear = fields[3]
# 	quantity = int(fields[4])
# 	if (quantity >=1):
# 		availableBooks[callno] = [bookName,author,pyear,quantity]
# for key,val in availableBooks.items():
#   print(key , " \t " , val[0] , " \t " , val[1], " \t\t " , val[2], " \t\t " , val[3])
#   # print(key,val[3])
# # print(availableBooks)