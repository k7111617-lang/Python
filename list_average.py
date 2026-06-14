list=[3,2,9,5,29,6,28,7]
print("Original list is", list)
count=0
for i in list:
    count+=i
avg=count/len(list)
print("sum is", count)
print("average is", avg)
list.sort()
print("The smallest element is", list[0])
print("The largest element is", list[-1])
print("The second largest element is", list[-2])