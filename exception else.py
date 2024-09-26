class apna_exception(Exception):
    pass    
def divide_two_nos(a, b):
    try:
        if b != 1 :
            c = a / b
            return c
        else:
            raise apna_exception
    except apna_exception:
        print("OK")        
divide_two_nos(5,1)
# class CustomError(Exception):
#     ...
#     pass
# 
# try:
#    ...
# 
# except CustomError: