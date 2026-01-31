maths=int(input("Enter math mark: "))
science=int(input("Enter science mark: "))
geography=int(input("Enter geography mark: "))
english=int(input("Enter english mark: "))
history=int(input("Enter history mark: "))
average=(maths+science+geography+history+english)/5
if average>=90 and average<=100:
    print("Grade is A1")
elif average>=80 and average<=89:
    print("Grade is A2")
elif average>=70 and average<=79:
    print("Grade is B1")
elif average>=60 and average<=69:
    print("Grade is B2")
elif average>=50 and average<=59:
    print("Grade is C1")
elif average>=40 and average<=49:
    print("Grade is C2")
elif average>=30 and average<=39:
    print("Grade is D1")
elif average>=20 and average<=29:
    print("Grade is D2")
elif average>=10 and average<=19:
    print("Grade is E1")
else: 
    print("Grade is E2")