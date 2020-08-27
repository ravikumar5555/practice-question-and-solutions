def sumPdivisors(num):
	sum = 0
	for i in range(1,num):
		if num % i == 0:
			sum += i
	return sum

def printPerfect(num_range):
	for n in range(1,num_range):
		if n == sumPdivisors(n):
			print(n)

number = int(input("Enter Number: "))
printPerfect(number)
