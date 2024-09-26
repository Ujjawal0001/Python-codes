password1 = 1234
Balance = 500000
b=True

def askPassword():
    password = int(input("Enter your password: "))
    if password == password1:
        askFromUser()
    else:
        print("Wrong password")
        b=False

def askFromUser():
    print("You have successfully checked in.")
    print("------------------------------------")
    print("Choose option:")
    print("1 for changing password")
    print("2 for checking balance")
    print("3 for debiting money")
    print("4 for crediting money")
    print("0 to exit")
    
    userInput = int(input())
    
    if userInput == 1:
        print("Enter new Password:")
        newPass = int(input())
        newpass_str = str(newPass)
        if len(newpass_str) == 4:
            changePassword(newPass)
        else:
            print("Password length is not valid")
    elif userInput == 2:
        checkBalance()
    elif userInput == 3:
        debit()
    elif userInput == 4:
        credit()
    elif userInput == 0:
        global b
        b = False  
    else:
        print("Invalid input")

def changePassword(newPass):
    global password1
    password1 = newPass
    print("Your new Password is :",password1)

def checkBalance():
    print("Your current balance is:", Balance)

def debit():
    global Balance
    global b
    print("Enter money you want to debit:")
    debitAmount = int(input())
    if(debitAmount>Balance):
        print("Incorrect amount")
        
    else:   
        Balance -= debitAmount
        print("Your Current Balance is:", Balance)

def credit():
    global Balance
    print("Enter money you want to credit:")
    creditAmount = int(input())
    Balance += creditAmount  
    print("Your Current Balance is:", Balance)
while b:
    askPassword()
print("Thank you for using the system.")
