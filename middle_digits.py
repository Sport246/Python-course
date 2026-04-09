num = int(input("Enter the number: "))
t = num
numLen = 0

while num > 0:
    numLen = numLen + 1
    t = int(t/10)
if numLen > 4:
    numLen = int(numLen/2)
    chk = 0
    while num > 0:
        rem = num%10
        if chk == numLen:
            mid1 = rem
        elif chk == (numLen - 1):
            mid2 = rem
        num = int(num/10)
        chk = chk + 1
    product = mid2*mid1
    print("The Product of Mid digits is (" + str(mid1)+ "*" + str(mid2)+ ") = ", product)
else:
    print("The given number is not 4 or more digits long")
    