char = input("Enter a single character: ")
if type(char) is str and len(char):
    # Get ASCII value
    ascii_val = ord(char)
    # Identify type
    print("\nCharacter Type: ", end="")
    if ascii_val >= 65 and ascii_val <= 122:
        print("Alphabet")

    elif ascii_val >= 48 and ascii_val <= 57:
        print("Number")

    elif ascii_val == 32:
        print("Space")

    else:
        print("Special Character")

else:
    print("\nError: Please enter exactly ONE character!")