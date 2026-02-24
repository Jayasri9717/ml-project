name = input("Enter student name: ")

m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

if percentage >= 90:
    grade = "o"
elif percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)