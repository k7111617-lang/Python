units=int(input("Enter the amount of units used: "))
if units<50:
    print("Per-unit cost is 2.60 plus 25 tax", (units*2.60)+25)
elif units>=50 and units<100:
    print("Per-unit cost is 3.25 plus 35 tax", (units*3.25)+35)
elif units>=100 and units<200:
    print("Per-unit cost is 5.26 plus 45 tax", (units*5.26)+45)
elif units >=200:
    print("Per-unit cost is 5.35 plus 50 tax", (units*5.35)+50)
else:
    print("Per-unit cost is 8.45 plus 75 tax", (units*8.45)+75)