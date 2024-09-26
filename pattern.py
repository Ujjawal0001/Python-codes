a=int(input())
#time complexity : 0(n)square
# for i in range(1,a+1):
#     for i in range(1,i+1):
#         print("*",end=" ")
#     print()
#time complexity : 0(n)
# for i in range(1,a+1):
#     print("*"*i)
# *
# * *
# * * *


for i in range(a,0,-1):
    for i in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(a,0,-1):
    print("* "*i)
#* * *
#* *
#*