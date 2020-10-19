# Job 31
print("This is job 31 :")
from math import ceil
def marks_rounder(grades):
    rounded_grades = []
    for g in grades:
        m = 5 * ceil(g/5)
        print(g, m, abs(m-g))
        if m - g < 3:
            rounded_grades.append(m)
        else:
            rounded_grades.append(g)
    return rounded_grades

print(marks_rounder([86, 83, 82, 45, 22, 10]))
