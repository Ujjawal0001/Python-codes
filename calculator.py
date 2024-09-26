print("Enter 1 to continue or 0 to exit")
a=int(input())
if(a==1):
    while(a==1):
        num1=int(input("Num1 : "))
        operator=input("Enter operator")
        num2=int(input("Num2 : "))
        if(num2!=0):
            if operator == "+":
                print(num1+num2)
            elif operator == "-":
                print(num1-num2)
            elif operator == "*":
                print(num1*num2)
            elif operator == "/":
                print(num1/num2)
            elif operator == "//":
                print(num1//num2)
            elif operator == "**":
                print(num1**num2)
            elif operator == "%":
                print(num1%num2)
            else:
                print("Wrong input")
        else:
            print("Num2 can not be zero")
        print("Enter 1 to continue or 0 to exit")
        a=int(input())

