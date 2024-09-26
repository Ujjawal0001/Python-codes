
def fact(a):
    facto=1
    while a>0:
        facto=facto*a
        a=a-1
    print(facto)
a=int(input())
fact(a)
