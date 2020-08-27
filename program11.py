def sumPdivisors(num):
	sum = 0
	for i in range(1,num):
		if num % i == 0:
			sum += i
	return sum


def printAmicable(num_range):
	for num in range(1,num_range):
		for n in range(1,num_range):
			if (sumPdivisors(num) == n) and (num == sumPdivisors(n)) and n != num :
				print(num, n)

number = int(input("Enter Number: "))
printAmicable(number)