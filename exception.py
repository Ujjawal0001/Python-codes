#  exceptions
# -- try/except
# -- else
# -- exception
# -- finally



a = 5
b = 1

print(a + b)
try:
    c = a / b
except ZeroDivisionError:
    print("you can't divide a number by zero")
except Exception:
    print("try again")    
else:
    print(c)
    
# print(6 + 9)
# try:
#     print('a' / 'b')

# # except Exception:
# #     print("Please try again later.")
# except ZeroDivisionError:
#     print("you can't divide a number by zero")
# # except TypeError:
# #     print("you can't divide two strings")    
# finally:
#     print("work done")
#     print("abc")