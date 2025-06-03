def fac1(n):
    ans=1
    while n>0:
        product=1*n
        n=n-1
        ans=product*ans
    print("Factorial ",ans)
    
    
def fac2(n):
    prod=1
    for i in range(2,n+1):
        prod=prod*i
    print("Factorial ",prod)
    
def fac3(n):
    if n==0:
        return 1
    return n*fac3(n-1)
    
    
n=int(input("Enter the digit: "))
fac1(n)
fac2(n)
print(fac3(n))
