import re

txt = "The rain in Spain"
x = re.search("\AThe", txt)
print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")