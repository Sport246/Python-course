import random
playing = True
num = str(random.randint(0, 9))

print("I will generate a number between 1 and 9. Your job is trying to gess which number I have chosen.")
print("The game will end when you get one right. Good Luck!!")
while playing:
    guess = input("Give me your best guess: ")
    if num == guess:
        print("You win the game!")
        print("The number was", num)
        break
    else:
        print("Wrong guess. Why don't you try again.")