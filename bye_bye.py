thing = False
while not thing:
    try:
        num = int(input("Enter a number: "))
        while num%2==0:

            print("bye")
        thing = True
    except ValueError:
        print("Invalid")