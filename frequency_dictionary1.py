a={"Jamal": 8, "is": 8, "the": 4, "best": 8, "smooth": 8, "operator": 6}
print("The original dictionary is: " + str(a))
K=int(input("Enter the desired frequency: "))
res=0
for key in a.values():
    if key==K:
        res+=1
    else:
        pass
print("The frequency of K is: " + str(res))