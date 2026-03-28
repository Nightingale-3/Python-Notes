import re

s = "geeks.forgeeks"

match = re.search(r'.', s)
print(match)

match = re.search(r'\.', s)
print(match)
