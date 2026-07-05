test_dict={"Jamal": 4, "is": 4, "super": 5, "duper": 4, "delicious": 4}
print("the original dictionary is: " + str(test_dict))
K=int(input("Enter the desired frequency: "))
res=0
for key in test_dict:
    if test_dict[key]==K:
        res+=1
    else:
        pass
print("The frequency of K is: " + str(res))