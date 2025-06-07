def small(v,l):
    ans=[]
    for i in l:
        if int(i)<v:
            ans.append(i)
    return ans


def small2(v,l):
    return[i for i in l if int(i)<v]


v=int(input("ENter the value: "))
l= input("Enter elements separated by space: ").split()
print(small(v,l))
print(small2(v,l))
