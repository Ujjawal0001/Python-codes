# def evensum(a) :
#     sum = 0 
#     for i in range(10):
#         if i % 2 == 0 :
#             sum = sum + i
#     return sum
# a = int (input("Enter number  :" ))
# sum = evensum(a)
# print(sum)

def evensum(a,b) :
    sum = 0 
    for i in range(a,b):
        if i % 2 == 0 :
            print(i)
            sum = sum + i
    print(sum)    
a = int (input("Enter number  :" ))
b = int (input("Enter number  :" ))
evensum(a,b)


