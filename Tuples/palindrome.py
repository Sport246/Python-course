def funktion(tup):
    end = len(tup) -1
    start = 0
    while(start<end):
        if(tup[start] != tup[end]):
            return False
        start+= 1
        end-= 1
    return True
tup = (3, 4, 8, 1, 7, 9)
if(funktion(tup)):
    print("The tuple is palindrome")
else:
    print("The tuple is not a palindrome")