def lcm(a,b):
    if a>b:
        a=a
    else:
        a,b=b,a
    for i in range(a,a*b+1):
        if (i%a)==0 and (i%b)==0:
            return i
    
a=int(input("Value of \'a\': "))
b=int(input("Value of \'b\': "))
print(lcm(a,b))
            