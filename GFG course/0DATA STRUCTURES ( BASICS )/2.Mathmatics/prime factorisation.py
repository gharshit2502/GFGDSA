def prime(a):
    if a <= 1:
        return False  
    for i in range(2, a ):
        if a % i == 0:
            return False  
    return True
    
def pf(n):
    l=[]
    for i in range(1,n+1):
       if (n%i==0) and (prime(i)) is True:
           l.append(i)
    return l

n = int(input("Enter the value: "))
print(pf(n))
    