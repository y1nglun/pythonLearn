import csv
import matplotlib.pyplot as plt

grades = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'F': 0
}

with open('midterm.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        score = float(row['Midterm'])
        # 这里多少分为什么等级没有给出,可以自行根据条件进行修改
        if score > 90:
            grades['A'] += 1
        elif score > 80:
            grades['B'] += 1
        elif score > 70:
            grades['C'] += 1
        elif score > 60:
            grades['D'] += 1
        else:
            grades['F'] += 1

grades_labels = grades.keys()
grades_counts = grades.values()

plt.bar(grades_labels, grades_counts)
plt.xlabel('Grade')
plt.ylabel('Count')
plt.title('Midterm Exam Grades')
plt.show()
