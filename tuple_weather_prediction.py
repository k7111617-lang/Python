tuple=(1,0,0,0,0,1,0,1,1,1)
s=tuple.count(0)
r=tuple.count(1)
if r>s:
    print("Rainy weather")
elif r==s:
    print("Neutral weather")
else:
    print("Sunny weather ")