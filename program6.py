#function that returns sum of cubes
def cubsum(num):
	sum = 0
	while num:
		digit = num % 10
		sum += digit**3
		num  = int(num/10)
	return sum


#function to check if number is armstrong number
def isArmstrong(num):
	if num == cubsum(num):
		return True
	else:
		return False


#function to print all armstrong numbers ib given range
def PrintArmstrong(num_range):
	for x in range(num_range):
		if isArmstrong(x): print(x)

number = int(input("Enter number: "))
PrintArmstrong(number)