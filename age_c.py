try:
    age = int(input("Enter your age: "))
    if age%2 == 0:
        print("The age is even")
    else:
        print("The number is odd")
except ValueError:
    print("Error!!! The value given is invalid")
