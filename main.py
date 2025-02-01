# This script programs what is your GWA
number = int(input("How many subjects/courses do you have? : "))
grade_lists = []
unit_lists = []
subject_names = []
x = 0
y = 0

for i in range(number):
    subject_name = str(input("Course: "))
    units_input = float(input("Unit/s: "))
    grades_input = float(input("Grade: "))
    print()
    y += units_input
    grade_lists.append(grades_input)
    unit_lists.append(units_input)
    subject_names.append(subject_name)
    grades_input *= units_input
    x += grades_input

z = x / y
print()
print("GWA: ", z)

if z < 1.5:
    print("President's Lister")
else:
    print("Dean's Lister")

# Tabulate the results
print("\n{:<20} {:<10} {:<10}".format("Course", "Units", "Grades"))
print("-" * 40)
for i in range(number):
    print("{:<20} {:<10} {:<10}".format(subject_names[i], unit_lists[i], grade_lists[i]))
print("-" * 40)
