s = input("Enter string: ").lower()

freq = {}

for ch in s:
    if ch.isalpha():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

for k in sorted(freq):
    print(freq[k], k.upper())