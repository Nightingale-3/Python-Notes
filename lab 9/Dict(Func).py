Dict = {"Roll_No" : "16/001", "Name" : "Arav", "Course" : "BTech"}
print("Name is: ", Dict.pop("Name"))
print("Dictonary after popping Name is: ", Dict)
print("Marks is: ", Dict.pop("Marks", -1))
print("Dictonary after popping Marks is: ", Dict)
print("Randomly popping an item: ", Dict.popitem())
print("Dictonary after random popping is: ", Dict) 
print("Aggregate is: ", Dict.pop("Aggr"))
print("Dictonary after popping Aggregate is: ", Dict)