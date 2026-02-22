string=input("Enter a string: ")
char=input("Enter a character: ")
i=0
count=0
while i<len(string):
    if string[i] == char:
        count+=1
    i+=1
print("number of repeated character is,", count)