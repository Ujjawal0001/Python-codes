n=int(input())
s=n
d=n
p=0
while(n!=0):
    p=p+1
    n=n//10

arm=0
while(s!=0):
    rem=s%10
    arm=rem**p+arm
    s=s//10
if(arm==d):
    print("armstrong")
else:
    print("no")
# if(p==s):
#     print("Palindrome")
# else:
#     print("no")