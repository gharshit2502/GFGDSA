def large(l):
    return(max(l))

def large1(l):
    for i in l:
        for j in l:
            if j>i:
                break
        else:
            return i
    return None
l= input("Enter elements separated by space: ")
print(large(l))
print(large1(l))