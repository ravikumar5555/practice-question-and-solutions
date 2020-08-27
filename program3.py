num = int(input("enter a number: "))
#list to store all factors(except 1) of entered number
factors = [x for x in range(2,num+1) if num%x == 0]
for n in factors:
	#if factor is prime, it will be printed
	for i in range(2,n):
		if n%i == 0:
			break
	else:
		print(n)