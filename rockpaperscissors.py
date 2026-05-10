import random
print("Welcome to the rock paper scissors game!")
choices=["rock", "paper", "scissors"]
computer=random.choice(choices)
user=input("Enter rock, paper or scissors:")
print("The computer chose,", computer)
if computer==user:
    print("It is a tie!")
elif computer=="rock":
    if user.lower()=="paper":
        print("User wins as paper beats rock")
    else: 
        print("Computer wins as rock beats scissors")
elif computer=="paper":
    if user.lower()=="scissors":
        print("User wins as scissors beats paper")
    else:
        print("Computer wins as paper beats rock")
elif computer=="scissors":
    if  user.lower()=="rock":
        print("User wins as rock beats scissors")
    else:
        print("Computer wins as scissors beats paper")
else:
    print("Please enter a valid input")