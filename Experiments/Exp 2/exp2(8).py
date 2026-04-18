name = ("Name: Rohit Sharma ")
roll = ("Roll Number: R17234512")
sapid = ("SAP ID: 50005673")
course = ("Course: B.Tech. CSE AI&ML")
sem = ("Semester: 1")

s1 = ("PDS = ", 70)
s2 = ("Python = ", 80)
s3 = ("Chemistry = ", 90)
s4 = ("English = ", 60)
s5 = ("Physics = ", 50)

total = s1[1] + s2[1] + s3[1] + s4[1] + s5[1]
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