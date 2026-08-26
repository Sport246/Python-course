def word_match(words):
    c = 0
    list = []
    for word in words:
        if len(word) >2 and word[0] == word[-1]:
            c += 1
            list.append(word)
    print("List of words with the first and last character same:", list)
    return c

count = word_match(["cjc", "5345", "94", "kak", "hdhf"])
print("Number of words with the first and last character same:", count)