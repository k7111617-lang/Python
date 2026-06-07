a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
def addition(a,b):
    return(a+b)

def subtraction(a,b):
    return(a-b)

def multiplication(a,b):
    return(a*b)

def division(a,b):
    try:
        c=a/b
        return(c)
    except ZeroDivisionError:
        return "There is an error!"
    except ValueError:
        return "There is a value error!"
    
choice=input("Enter which operation you would like to choose:")
if choice=="addition":
    print(addition(a,b))
elif choice=="subtraction":
    print(subtraction(a,b))
elif choice=="multiplication":
    print(multiplication(a,b))
else:
    print(division(a,b))

