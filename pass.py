num = input("Enter a number: ")
for i in range(10):
    if i%15 == 0:
        print("twist")
    elif 1%15 == 0:
        pass
    elif i%5 == 0:
        print("fizz")
    elif i%3 == 0:
        print("buzz")
    else:
        print(i)