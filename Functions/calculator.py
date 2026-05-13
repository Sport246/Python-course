def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def divide(P,Q):
    return P / Q
def multiply(P,Q):
    return P * Q
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Select which operation to be used: ")
print("a = Addition")
print("b = Subtraction")
print("c = Division")
print("d = Multiplication")
opp = input("Enter the choise: ")
if opp == "a":
    print(add(num1,num2))
elif opp == "b":
    print(subtract(num1,num2))
elif opp == "c":
    print(divide(num1,num2))
elif opp == "d":
    print(multiply(num1,num2))