def rev1(s):
    n=str(s)
    ans=n[::-1]
    print("Reversed1 :",ans)
    
def rev2(s):
    ans,d,s=0,0,abs(s)
    while s>0:
        d=s%10
        s=s//10
    
        ans=d+ans*10
    print("Reversed2 :",ans)

s=int(input("Enetr the number: "))
rev1(s)
rev2(s)