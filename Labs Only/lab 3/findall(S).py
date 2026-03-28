import re 

txt = "The rain in Spain"

x = re.findall("\S", txt)
print(x)

if x:
    print("Yes, there is atleast one match!")
else:
    print("No match")
    