def Sum_Of_Primes(n):

	prime = [True] * (n + 1)
 
	
	s = 2

	while s * s <= n:

		if prime[s] == True:

			i = s * 2
			while i <= n:
				prime[i] = False
				i += s
		s = s + 1
		

	sum = 0
	for i in range (2, n + 1):
		if(prime[i]):
			sum = sum + i
	return sum

n = int(input("\nPlease enter limit:"))
print("\n The sum of prime numbers " , n, "is : ",Sum_Of_Primes(n))