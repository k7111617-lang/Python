medical_cause=input("Do you have a medical cause Y or N?")
if medical_cause=='Y':
    print("Excused")
else:
    atten=int(input("Enter your attendance: "))
    if atten>=75:
       print("Allowed")
    else:
        print("Not allowed")