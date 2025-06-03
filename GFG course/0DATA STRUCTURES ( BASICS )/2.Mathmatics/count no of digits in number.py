
def count1(n):
    c=0
    while n>0:
        c=c+1
        n=n//10
    print("count1= ",c)

def count2(n):
    n=str(n)
    c=len(n)
    print("count2= ",c)
    
n=int(input("ENter the number: "))
count1(n)
count2(n)