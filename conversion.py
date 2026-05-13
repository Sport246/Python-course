def kmiles(km):
    return km * 0.62
def temperature(c):
    return (c * 9/5) + 32
def weight(kg):
    return kg * 2.2

print("Welcome to the Global Conversion.")
num1 = int(input("Enter the first number to be converted: "))

print("Here are the Conversions availible: ")
print("a = Kilometeres to Miles")
print("b = Celsius to Fahrenheit")
print("c = Kilograms to Pounds")
conv = input("Choose a Conversion: ")

if conv == "a":
    print(kmiles(num1))
if conv == "d":
    print(temperature(num1))
if conv == "c":
    print(weight(num1))