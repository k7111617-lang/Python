a=int(input("Enter speed 1: "))
b=int(input("Enter speed 2: "))
c=int(input("Enter speed 3: "))
avg=(a+c+b)/3
print("The average is",avg)
if avg>a and avg>b:
    print("avg is greater than a and b")
elif avg>b and avg>c:
    print("avg is greater than b and c")
elif avg>a and avg>c:
    print("avg is greater than a and c")
elif avg>a:
    print("avg is greater than a")
elif avg>b:
    print("avg is greater than b")
elif avg>c:
    print("avg is greater than c")
