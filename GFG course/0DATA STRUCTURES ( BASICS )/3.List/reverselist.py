def rev1(l):
    return l[::-1]

def rev2(l):
    r=[]
    i = len(l) - 1
    while i>=0:
        r.append(l[i])
        i=i-1
    return r

def rev3(l):
    l.reverse()
    return l

    
    
l= input("Enter elements separated by space: ").split()
print(rev1(l))
print(rev2(l))
print(rev3(l))
