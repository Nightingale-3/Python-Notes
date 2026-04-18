n = int(input("Enter number of values: "))
lst = list(map(int, input("Enter values (0-3): ").split()))

count = [0, 0, 0, 0]

for x in lst:
    if 0 <= x <= 3:
        count[x] += 1

for i in range(4):
    print(i, "occurs", count[i], "times")