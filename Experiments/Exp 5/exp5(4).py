n = int(input("Enter number of persons: "))
d = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    d[name] = city

print("\nAll names:")
for k in d:
    print(k)

print("\nAll cities:")
for v in d.values():
    print(v)

print("\nName and City:")
for k, v in d.items():
    print(k, "-", v)

print("\nStudents in each city:")
count = {}
for v in d.values():
    count[v] = count.get(v, 0) + 1

for city in count:
    print(city, ":", count[city])