tup = "abcdxxxabcdxxxabcdxxx"
print ("x appears", tup.count("x"), "times in", tup)

def double(T):
    return ([i * 2 for i in T])

Tup = 1, 2, 3, 4, 5
print("Original Tuple:", Tup)
print("Double Values: ", double(Tup))