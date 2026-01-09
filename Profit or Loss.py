boughtamount = float(input("Enter Price of bought Product: "))
sellamount = float(input("Enter selling Price: "))
differnce = (sellamount - boughtamount)
if sellamount>boughtamount:
    print("Profit is ", differnce)
else:
    print("Loss is", differnce)