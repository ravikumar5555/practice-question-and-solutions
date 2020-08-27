def sumPdivisors(num):
	sum = 0
	for i in range(1,num):
		if num % i == 0:
			sum += i
	return sum

number = int(input("Enter Number: "))
print("Sum: ",sumPdivisors(number))