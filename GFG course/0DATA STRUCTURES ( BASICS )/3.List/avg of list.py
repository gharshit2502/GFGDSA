
def avg(l):
    no=len(l)
    sum=0
    for i in l:
        sum+=i

    print(sum/no)
   
# l=int(input("Eter the list"))
l= list(map(int, input("Enter the list elements separated by space: ").split()))
avg(l)     