def tip_waiter(amount):
    tip=amount*0.15
    total=amount+tip
    print(total)
amount=int(input("Enter the total amount: "))
tip_waiter(amount)
