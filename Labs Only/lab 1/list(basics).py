L2 = ["Delhi", "Mumbai", "Chennai"]
print(L2[0:2])

list = [10,20,30,40,50,60]
print(list[::2])
print(list[4:])
print(list[:3])
print(list[:])
print(list [-1])


i = 0
while i < 4:
    print(list[i], end = " ")
    i = i + 1

for i in list:
    print(i, end = " ")

while i < len(list):
    print(list[i], end = " ")
    i = i + 1

L = len(list)
while i < L:
    print(list[i], end = " ")
    i = i + 1