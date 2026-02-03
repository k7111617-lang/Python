choice1=input("What mode of transport do you prefer, car or bike?")
if choice1=='car':
    print("You have chosen car:")
    choice2=input("What car brand: Cheetos, Pringles or Ketchup?")
    if choice2=='Cheetos':
        print("You have chosen Cheetos")
    elif choice2=='Pringles':
        print("You have chosen pringles")
    else:
        print("You have chosen Ketchup")
elif choice1=='bike':
    print("You have chosen bike")
    choice3=input("What type of bike, Bones or muscle?")
    if choice3=='Bones':
        print("You have chosen Bones")
    else:
        print("You have chosen muscle")
else:
    print("Invalid input")

    