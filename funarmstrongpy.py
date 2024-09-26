
def count(a):
    c=0
    while a>0:
        a=a//10
        c=c+1
    return c
def armstrong_number(a):
    sum=0
    check=a
    while a>0:   
        rem=a%10
        sum=sum+rem**count(check)
        a=a//10
    if check==sum:
        print(check,"is an armstrong number")
    else :
        print(check,"is not an armstrong number")        
a=int(input("Enter number : "))
armstrong_number(a)
