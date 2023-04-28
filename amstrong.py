
def is_Armstrong(A):  
        
  
    temp_1 = A  
    sum_1 = 0  
        
    while (temp_1 != 0):  
        R_1 = temp_1 % 10  
        
        temp_1 = temp_1 // 10  
    
  
    return (sum_1 == A)  
    
 
A = int(input("Please enter the number to be checked: "))  
print(is_Armstrong(A))  