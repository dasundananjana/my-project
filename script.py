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

print(f"Your grade is: {grade}")

