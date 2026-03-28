l = [1,2,4,5,3,7,8,2,8,10]

for i in range(len(l) - 1, -1, -1):
    if l[i] % 2 == 0:
        l.remove(l[i])
        
print(l)