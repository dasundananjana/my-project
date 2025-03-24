num_students = int(input("Enter number of students: "))

for i in range(num_students):
    print(f"\nStudent {i+1}")
    marks = int(input("Enter English marks: "))

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

    print(f"Grade for student {i+1}: {grade}")

