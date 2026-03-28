fruit1 = input("Enter the name of the first fruit: ")
fruit2 = input("Enter the name of the second fruit: ")

if fruit1 < fruit2:
    print(fruit1, "comes before", fruit2, "in the dictonary.")
elif fruit1 > fruit2:
    print(fruit2, "comes after", fruit1, "in the dictonary.")
else:
    print(fruit1, "and", fruit2, "are the same.")