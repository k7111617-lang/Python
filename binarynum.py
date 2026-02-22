decimal_num = int(input("Enter the decimal number: "))
binary_num = ""

while decimal_num > 0:
    remainder = decimal_num % 2
    binary_num = str(remainder) + binary_num
    decimal_num = decimal_num//2 

print("The binary equivalent is:", binary_num)