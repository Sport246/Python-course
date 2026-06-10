try:
    num = int(input("Enter a number: "))
    print("The number enterd is",num)
except ValueError as ex:
    print("Exception:",ex)