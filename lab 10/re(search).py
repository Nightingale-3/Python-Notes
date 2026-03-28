import re 

string = "She sells sea shells by the sea shore."

pattern = "sells"
if re.search(pattern, string):
    print("Match found!")
else:
    print(f"{pattern} not found in the string.")