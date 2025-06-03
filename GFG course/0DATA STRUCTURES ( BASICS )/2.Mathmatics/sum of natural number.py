def sum1(n):
    ans=(n*(n+1)/2)
    print(ans) 

def sum2(n):
    ans=0
    for i in range(0,n+1):
        ans=ans+i
    print(ans) 


print("SUm of First \"n\" natural numnber")
n=int(input("Enetr the number: "))
sum1(n)
sum2(n) 