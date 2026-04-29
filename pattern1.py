print("Half Pyramid Pattern of Stars (*): ")
r = int(input("Enter number of rows: "))
for i in range(r):
    for j in range(i+1):
        print("*", end="")
    print()