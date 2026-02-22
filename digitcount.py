num=int(input("Enter a number: "))
temp=num
digitcount=0
if num==0:
    digitcount=1
else:
    while temp>=0:
      digitcount+=1
      temp=temp//10
print("digitcount is", digitcount)