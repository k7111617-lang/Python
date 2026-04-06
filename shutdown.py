choice = input("Do you want to shut down the computer? (yes/no): ")
def shutdown(choice):
    if choice=="yes":
        print("Computer is shutting down")
    else:
        print("Computer is not shutting down")
shutdown(choice)