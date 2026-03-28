import re

line = "pet: cat i love cat pet: cow i love cow"
match = re.findall(r"pet:\w\w\w", line)
print(match) 