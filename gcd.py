a = int(input("Enter the first number: "))
b = int(input("Enter the second number:"))
og_a = a
og_b = b
while b!= 0:
    a,b = b, a % b
print("The GDC of", og_a, "and", og_b, "is", a)