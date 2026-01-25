costprice=int(input("Enter the cost price: "))
sellingprice=int(input("Enter the selling price: "))
if sellingprice>costprice:
    print("Profit is", sellingprice-costprice)
elif costprice>sellingprice:
    print("Loss is", costprice-sellingprice)
else:
    print("no profit or loss")