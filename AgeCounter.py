try:
    age=int(input("Enter your age: "))
    print("The age is,", age)
    if age%2==0:
        print("Age is even")
    else:
        print("Age not even")
except ValueError as ex:
    print("Exception", ex)