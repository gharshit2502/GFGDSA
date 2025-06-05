def div(n):
    l=[]
    for i in range(1,n+1):
        
        if n%i==0:
            l.append(i)
    print(l)



def div1(n):
    i=1
    while (i*i<=n):
        if (n%i)==0:
            print(i)
            if (i!=n/1):
                print(n/i)
        i+=1
        
        
        
        
n = int(input("Enter the value: "))
div(n)
div1(n)