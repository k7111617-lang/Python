a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
L=[]
odd_list=[]
even_list=[]
for i in range(a,b+1):
    L.append(i**2)
for i in L:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("The original list was", L)
print("The even list is", even_list)
print("The odd list is", odd_list)