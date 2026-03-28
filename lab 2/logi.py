a = 5
b = 10

ret = ( (a <= b) and (a != b) )
print("Return Value of the first expression is : ", ret)

ret = ( (a >= b) or (a == b) )
print("Return Value of the second expression is : ", ret)

ret = not ( (a < b) and (a == b) )
print("Return Value of the third expression is : ", ret)