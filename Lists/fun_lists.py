l = [4, 9, 2, 7 ,5, 1, 3,]
print("Original list:", l)
count = 0
for i in l:
    count += 1
avg = count/len(l)
print("Sum =", count)
print("Average =", avg)
l.sort()
print("Smallest element is:", l[0])
print("Largest element is:", l[-1])