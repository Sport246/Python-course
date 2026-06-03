while True:
    amt = int(input("Enter the transaction amount: "))
    if amt == 0:
        pass
    elif amt < 0:
        print("Error")
        continue
    elif amt >500:
        print("Security Alert!")
        break
    else:
        print("Transaction processed successfully")