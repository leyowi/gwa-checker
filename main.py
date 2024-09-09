# This script programs what is your GWA
print("INSTRUCTION: Enter first your subject then your grades and its respective units.")
print()
number = int(input("How many is your subjects / courses? : "))
grade_lists = []
unit_lists = []
x = 0
y = 0

for i in range(number):
    subject_name = str(input("Subject name / code: "))
    grades_input = float(input("Grade of this subject : "))
    units_input = float(input("Unit/s of this subject: "))
    print()
    y += units_input
    grade_lists.append(grades_input)
    unit_lists.append(units_input)
    grades_input *= units_input
    x += grades_input

z = x / y
print()
print("GWA: ", z)

if z <= 1.0:
    print("= 97-100")
    print("Excellent")
elif z <= 1.25:
    print("= 94-96")
    print("Excellent")
elif z <= 1.5:
    print("= 91-93")
    print("Very Good")
elif z <= 1.75:
    print("= 88-90")
    print("Very Good")
elif z <= 2.0:
    print("= 85-87")
    print("Good")
elif z <= 2.25:
    print("= 82-84")
    print("Good")
elif z <= 2.5:
    print("= 79-81")
    print("Satisfactory")
elif z <= 2.75:
    print("= 76-78")
    print("Satisfactory")
elif z <= 3.0:
    print("= 75")
    print("Passed")
else:
    print("Failed")