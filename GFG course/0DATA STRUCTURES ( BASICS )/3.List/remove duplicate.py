# def duplicate(l):
#     size=len(l)
#     temp=[]
#     for i in l:
#         for j in l:
#             if i==j:
#                 continue
#             else:
#                 l.append(i)
#     return l

def duplicate(l):
    temp = []
    for item in l:
        if item not in temp:
            temp.append(item)
    return temp

l= input("Enter elements separated by space: ").split()
print(duplicate(l))