import random
print("Welcome to the Number Game!")
computer=random.randint(0,10)
userinput=int(input("Enter a number between 0 and 10:"))
if userinput==computer:
    print("You won the game!")
else:
    print("You lost the game")
    print("The computer's number was", computer)