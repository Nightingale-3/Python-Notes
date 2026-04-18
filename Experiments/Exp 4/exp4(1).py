s = input("Enter string: ")
count = 0

for ch in s:
    if ch.isupper():
        count += 1

print("Capital letters:", count)