a=input("Enter number : ")
prime=0
a=int(a)
i=2
while  i<=a//2:
    if a%i==0:
        prime=1
        break
    i=i+1
if prime==0:
    print(a,"is a prime number")
else :
    print(a,"is not a prime ")

        