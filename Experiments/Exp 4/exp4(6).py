s = input("Enter sentence: ")

words = s.split()
unique = set(words)

print("Unique words count:", len(unique))