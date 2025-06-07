def evod(l):
    el,ol=[],[]
    # ol=[]
    for i in l:
        (el if int(i) % 2 == 0 else ol).append(i)
    return el, ol
l= input("Enter elements separated by space: ").split()
print(evod(l))