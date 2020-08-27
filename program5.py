#using bin()
num = int(input("Enter a number: "))
print(bin(num))

#not using inbuiilt function
def findBinary(num):
	binary_num = ""
	while num:
		binary_num+=str(num%2)
		num = int(num/2)
	print(binary_num[::-1])

findBinary(num)