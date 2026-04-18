d = {"a": 10, "b": 10, "c": 10}

check = lambda x: len(set(x.values())) == 1

print("All same:", check(d))