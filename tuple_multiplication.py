a=(3, 4, 6, 7, 8, 9)
print("Original tuple is", a)
result=1
for i in range(len(a)):
    result=result*a[i]
print("The multiplication of all the elements comes out to", result)