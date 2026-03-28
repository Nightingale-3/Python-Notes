num_list = [1,2,3,4,5,6,7,8,9,10]
print("num_list is: ", num_list)
print("First element in the list is ", num_list[0])
print("num_list[2:5] = ", num_list)
print("num_list[::2] = ", num_list)
print("num_list[1::3] = ", num_list)

num_list[5] = 100
print("List after updation is: ", num_list)

num_list.append(200)
print("List after appending a value is ", num_list)

del num_list[3]
print("List after deleting a value is ", num_list)