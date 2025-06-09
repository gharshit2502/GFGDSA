def rotate(l):
    size=len(l)
    temp=l[0]
    for i in range(1,size):
        l[i-1]=l[i]
    l[size-1]= temp
    return l

def rotate1(l):
   return l[1:] + l[:1]
    # return l[1:]+ l[:1]
   

l= input("Enter elements separated by space: ").split()
print(rotate(l))
print(rotate1(l))