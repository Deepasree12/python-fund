def getSum(n):
    
    n =int(input('enter a number'))
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
n = 0
print(getSum(n))