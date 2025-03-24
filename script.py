num_students = int(input("Enter number of students: "))
student_grades = {}

for i in range(num_students):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = int(input(f"Enter English marks for {name}: "))

    if marks >= 75:
        grade = "A"
    elif marks >= 65:
        grade = "B"
    elif marks >= 55:
        grade = "C"
    elif marks >= 35:
        grade = "S"
    else:
        grade = "F"

    student_grades[name] = grade
    print(f"Grade for {name}: {grade}")

print("\n--- Grade Summary ---")
for name, grade in student_grades.items():
    print(f"{name}: {grade}")
