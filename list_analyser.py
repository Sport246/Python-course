mt_list = []
print(mt_list)

marks = [96, 83, 72, 86, 88]
print("Student marks:", marks)

sample = [30, 20, 10] * 2
print("Sample marks:", sample)
print("Number of marks", len(marks))
print("First mark:", marks[0])
print("Last mark:", marks[-1])

first_3 = marks[0:3]
print("First three marks:", first_3)

reverse = marks[::-1]
print("Marks revesered is:", reverse)

def match_marks(mark_list):
    count = 0
    matched_marks = []
    for mark in mark_list:
        mark_text = str(mark)
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)
    print("Marks with first and last digits same:", matched_marks)
    return count
same_digit_count = match_marks([96, 83, 72, 86, 88])
print("Number of matching marks:", same_digit_count)

total = 0

for mark in marks:
    total += mark

avg = total /len(marks)

print("Sum of marks:", total)
print("Average marks:", avg)

print("")
print("===== STUDENT MARKS LIST ANALYSER =====")
print("Sorted Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", avg)
print("Lowest Mark:", marks[0])
print("Highest Mark:", marks[-1])
print("=======================================")