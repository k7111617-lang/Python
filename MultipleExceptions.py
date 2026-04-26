try:
    num1, num2=eval(input("Enter 2 numbers seperated by a comma: "))
    result=num1/num2
    print("The result is", result)
except ZeroDivisionError:
    print("Division by 0 Error")
except SyntaxError:
    print("Comma not given")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")