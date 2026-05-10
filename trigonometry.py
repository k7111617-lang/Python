import math
angle=float(input("Enter the angle in degrees: "))
radians=math.radians(angle)
sin_value=math.sin(radians)
cos_value=math.cos(radians)
tan_value=math.tan(radians)
print("sin(",radians,") is =", sin_value)
print("cos(",radians,") is =", cos_value)
print("tan(",radians,") is =", tan_value)