word=input("Enter a word: ")
for i in word.lower():
    if i == 'a':
        print("a is found")
        break
    else:
        print("a not found")