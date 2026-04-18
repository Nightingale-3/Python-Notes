s1 = set(input("Enter fruits for set1: ").split())
s2 = set(input("Enter fruits for set2: ").split())

print("Common fruits:", s1 & s2)
print("Only in s1:", s1 - s2)
print("Total fruits count:", len(s1 | s2))