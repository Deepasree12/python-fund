def fun(n):  
    sum = 0  
    i = 2  
    while i <= n:  
        sum += i  
        i = i + 2  
    return sum  
      
n = int(input('Enter any number: '))  
print("Sum of all even numbers from 1 to", n , "is: " , fun(n))