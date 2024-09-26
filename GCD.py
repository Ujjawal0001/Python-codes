a=int(input())
b=int(input())
min1=min(a,b)
while(min1>=1):
    if(a%min1==0 and b%min1==0):
        print("GCD :",min1)
        break
    min1=min1-1
        