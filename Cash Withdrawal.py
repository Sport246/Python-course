cash = int(input("Enter your desired cash withdrawal: "))
amount_of_100 = cash//100
remainder1 = cash%100
amount_of_50 = remainder1//50
remainder2 = remainder1%50
amount_of_10 = remainder2//10

print(amount_of_100)
print(amount_of_50)
print(amount_of_10)