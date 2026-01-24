amount=int(input("enter amount for withdrawal: "))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("number of 100 notes", note1)
print("number of 50 notes", note2)
print("number of 10 notes", note3)