def hcf1(a,b):
    a,b=abs(a),abs(b)
    while b:
        a,b=b,a%b
    return a

def hcf2(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def hcf3(a,b):
    if b==0:
        return a
    return hcf3(b,a%b)
    
    
    
a=int(input("Value of \'a\'"))
b=int(input("Value of \'b\'"))
print(hcf1(a,b))
print(hcf2(a,b))
print(hcf3(a,b))
