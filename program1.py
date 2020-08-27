#function to print multiplication table of number
def printTable(num):
	for n in range(1,11):
		print("{}x{}={}".format(num,n,num*n))

#accepting input
num = int(input("Enter a number to print table: "))

#caling function with given input
printTable(num)