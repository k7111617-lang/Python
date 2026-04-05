def factorial(x):
    """This is the factorial of an integer"""
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
x=int(input("Enter the desired number: "))
print(factorial.__doc__)
print(factorial(x))