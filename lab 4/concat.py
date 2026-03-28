str1 = "Hello"
print("Str1 is: ", str1)
print("ID of str1 is: ", id(str1))

str2 = "World"
print("\nStr2 is: ", str2)
print("ID of str2 is: ", id(str2))

str1 += str2
print("\nStr1 after concatenation is: ", str1)
print("ID of str1 after concatenation is: ", id(str1))

str3 = str1
print("\nStr3 is: ", str3)
print("ID of str3 is: ", id(str3))