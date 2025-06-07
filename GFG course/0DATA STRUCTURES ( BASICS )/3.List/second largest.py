def secl(l):
    size=len(l)
    largest=0
    seclarge=0
    if size == 0 or size==1:
        return None
    else:
        for i in l:
            if i> str(largest):
                seclarge=largest
                largest =i
        return seclarge


l= input("Enter elements separated by space: ")
print(secl(l))