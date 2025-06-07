def check(l):

    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            return False   
    return True
    
def check1(l):
    sr=sorted(l)
    if sr== l:
        return True
    return False 
 
l= input("Enter elements separated by space: ")
# print(check(l))
print(check1(l))