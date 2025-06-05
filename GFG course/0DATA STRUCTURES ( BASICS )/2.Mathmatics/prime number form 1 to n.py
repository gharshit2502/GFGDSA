def prime(a):
    if a <= 1:
        return False  
    for i in range(2, a ):
        if a % i == 0:
            return False  
    return True

def primen(n):   
    l=[]
    for i in range(1,n):
        if prime(i) is True:
            l.append(i)
    print(l)
        
def primen1(n):
    l=[]
    for i in range(2,n+1):
        if (i%2==0) or (i%3==0) or (i%5==0) or (i%7==0):
            # print()
            continue
        else:
            l.append(i)
            
    print([1,2,3,5] +l) 
            
            
    
    
    
    
    
n=int(input("ENetr the number: "))
# primen(n)
primen1(n)

