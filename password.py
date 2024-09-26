def askPassword():
    password=input("Enter your password :")
    checkPassword(password)
def checkPassword(password):
    flag_upper=0
    flag_lower=0
    flag_num=0
    flag_symbol=0
    if len(password)>=8:
        for char in password:
            if char.isupper():
                flag_upper+=1
            elif char.islower():
                flag_lower+=1
            elif char.isdigit():
                flag_lower+=1
            else:
                flag_symbol+=1
    else:
        print("Your password must contain 8 digits")
    if(flag_upper==0):
        print("Upper case is missing")
    if(flag_lower==0):
        print("Upper case is missing")
    if(flag_num==0):
        print("Number is missing")
    if(flag_symbol==0):
        print("Symbol is missing")
askPassword()
