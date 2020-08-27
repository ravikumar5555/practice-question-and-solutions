def prodDigits(num):
	product = 1
	while num:
		digit = num % 10
		product*=digit
		num = int(num/10)
	return product

def MDR(num):
	product = prodDigits(num)
	while len(str(product)) > 1:
		product = prodDigits(product)
	return product

def MPersistence(num):
	count = 1
	product = prodDigits(num)
	while len(str(product)) > 1:
		count += 1
		product = prodDigits(product)
	return count

number = int(input("Enter Number: "))
print("MDR: ",MDR(number))
print("MPersistence: ", MPersistence(number))	
