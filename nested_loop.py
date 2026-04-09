word = str(input("Enter a word: "))
letter = str(input("Enter a character: "))
count = 0
i = 0
while(i < len(word)):
    if word[i] == letter:
        count = count + 1
    i = i + 1
print("The amount of", count, "are in", word)
