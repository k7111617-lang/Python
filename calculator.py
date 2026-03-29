def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
x=int(input("Enter a number: "))
y=int(input("Enter another number"))
decision=input("Enter the operation:")
if decision=="+":
    print(add(x,y))
elif decision=="-":
    print(subtract(x,y))
elif decision=="*":
    print(multiply(x,y))
else: 
    print (divide(x,y))
    