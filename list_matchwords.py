def match_word(words):
    ctr=0
    lst=[]
    for i in words:
        if len(i)>2 and i[0]==i[-1]:
            ctr+=1
            lst.append(i)
    print("The number of eligible elements is", ctr)
    print("The elements that fulfilled the criteria are", lst)
myList=['aba','koj','lal','jon','mamamamam','pop', '808']
match_word(myList)
