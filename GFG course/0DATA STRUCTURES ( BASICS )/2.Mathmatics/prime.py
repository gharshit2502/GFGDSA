def prime(a):
    if a <= 1:
        return False  
    for i in range(2, a ):
        if a % i == 0:
            return False  
    return True
    
    

n = int(input("Enter the value: "))
# print(prime(n))
print("true") if prime(n) else print("fasle")

