number=int(input("Enter the number: "))
power = int(input("Enter the power: "))
result = 1
for i in range(power):
    result = result * number

print("Answer:", result)
