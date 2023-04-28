n=int(input("enter a limit"))

for i in range(1,n):
     if not i % 5 or not i % 3:
         n = n + i
print(n)