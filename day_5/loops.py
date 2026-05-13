# for loop demonstration
marks = [45,56,87,156,35,44,78,99,456,345,245,345,68,234,457,367,167,169,136,155,177,180]

len_marks= len(marks)
print(len_marks)
sum_marks = sum(marks)
max_marks= max(marks)
print(sum_marks)
print(max_marks)

for mark in marks:
    print(mark)

m = 0
for mark in marks:
    m += mark
print(m)
s = 0
for mark in marks:
    if mark > s:
        s = mark
print(s)


