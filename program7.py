def prodDigits(num):
	product = 1
	while num:
		digit = num % 10
		product*=digit
		num = int(num/10)
	return product

print(prodDigits(249))