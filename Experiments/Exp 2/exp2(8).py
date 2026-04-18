name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
sapid = input("Enter SAP ID: ")
course = input("Enter Course: ")
sem = input("Enter Semester: ")

print("\nEnter marks of 5 subjects:")

s1 = int(input("PDS: "))
s2 = int(input("Python: "))
s3 = int(input("Chemistry: "))
s4 = int(input("English: "))
s5 = int(input("Physics: "))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5
cgpa = percentage / 10

if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"

print("\n----- Grade Sheet -----")
print("Name:", name)
print("Roll Number:", roll)
print("SAP ID:", sapid)
print("Course:", course)
print("Semester:", sem)

print("\nMarks:")
print("PDS:", s1)
print("Python:", s2)
print("Chemistry:", s3)
print("English:", s4)
print("Physics:", s5)

print("\nPercentage:", percentage, "%")
print("CGPA:", cgpa)
print("Grade:", grade)