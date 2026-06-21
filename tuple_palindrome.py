r=(1,2,3,5,4,3,2,1)
def palind(r):
    e=len(r)-1
    s=0
    while (s<e):
        if r[s]!=r[e]:
            return False
        else:
            e-=1
            s+=1
    return True
if palind(r):
    print("The tuple is a palindrome")
else:
    print("The tuple isn't a palindrome.")