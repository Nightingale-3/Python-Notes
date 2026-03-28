Dict = {"Roll_No" : "16/001", "Name" : "Arav", "Course" : "BTech"}
print(Dict,"\n")

print("Dict [ROLL_NO] =", Dict["Roll_No"])
print("Dict [Name] =", Dict["Name"])
print("Dict [Course] =", Dict["Course"])
Dict["Marks"] = 95
print("Dict [Marks] =", Dict["Marks"])

Dict["Course"] = "BCA"
print("Dict [Course] =", Dict["Course"])