a= int(input())
for i in range(a):
    for j in range(i):
        print("*",end="")
        j=j+1    
    i=i+1
    print()