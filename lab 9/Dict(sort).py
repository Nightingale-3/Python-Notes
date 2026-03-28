Dict = {"Roll_No" : "16/001", "Name" : "Arav", "Course" : "BTech"}
print(sorted(Dict.keys()))

print("\nKEYS: ", end = " ")
for key in Dict.keys():
    print(key, end = " ")

print("\n\nVALUES: ", end = " ")
for val in Dict.values():
    print(val, end = " ")

print("\n\nDICTIONARY: ", end = " ")
for key, val in Dict.items():
    print(key, val, "\t", end = " ")