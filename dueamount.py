def dueamount():
    total_amount=int(input("Enter the total amount: "))
    paid=int(input("How much have you paid so far: "))
    dueamount=total_amount-paid
    print("Your total due amount is", dueamount)
dueamount()