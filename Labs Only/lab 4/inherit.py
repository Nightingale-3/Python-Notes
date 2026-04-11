class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, exp, r_area):
        Person.__init__(self, name, age)
        self.exp = exp
        self.r_area = r_area
    def displayData(self):
        Person.display(self)
        print(f"Experience: {self.exp}")
        print(f"Research Area: {self.r_area}")

class Student(Person):
    def __init__(self, name, age, course, marks):
        Person.__init__(self, name, age)
        self.course = course
        self.marks = marks
    def displayData(self):
        Person.display(self)
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

print("********** Teacher ***********")
T = Teacher("Jaya", 43, 20, "Recommender Systems")
T.displayData()
print("********** Student ***********")
S = Student("Mani", 20, "BTech", 78)
S.displayData()