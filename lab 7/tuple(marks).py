def max_min(vals):
    x = max(vals)
    y = min(vals)
    return(x, y)

vals = (99, 98, 90, 97, 89, 86, 93, 82)
(max_marks, min_marks) = max_min(vals)
print("Highest Marks =", max_marks)
print("Lowest Marks =", min_marks)

print("\n")

Toppers = (("Arav", "BSc", 92.0), ("Chaitanya", "BCA", 99.0), ("Druvika", "BTech", 97))
for i in Toppers:
    print(i)