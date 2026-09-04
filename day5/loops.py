student_scores = [42, 87, 15, 63, 91, 28, 54, 76, 3, 69, 81, 35, 99, 12, 50, 74, 22, 88, 60, 45]
max = 0 
for scores in student_scores:
    if scores > max:
        max = scores

print(max)