#function to find factorial. I have used recursion
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num-1)

#function to find permutations
def permutations(n,r):
	print("permutations p({},{}): {}".format(n,r,int(facto(n)/facto(n-r))))
	return(int(facto(n)/facto(n-r)))

#function to find combinations
def combinations(n,r):
	print("combinations c({},{}): {}".format(n,r,int(permutations(n,r)/facto(r))))

combinations(5,2)

