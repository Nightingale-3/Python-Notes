list_A = [1,2,3,4,5]
print(list_A)

list_C = ["Good", "Going"]
print(list_C)

list_B = ["A", "B", "C", "d", "E"]
print(list_B)

list_D = [1, "a", "bcd"]
print(list_D)

list_E = list_A [:]
print(list_E)

list_F = list_A [0:2]
print(list_F)

# list compression

S = [x**2 for x in range(10)]
print(S)

A =[3,4,5]
B = [value*3 for value in A]
print(B)

C = []
for i in A:
    C.append(i*3)

print(C)

D = [i for i in S if i % 2 == 0]
print(D)

l = list()
print (l) 

E = F = [10,20,30]
print(E, F)