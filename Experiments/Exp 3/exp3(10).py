n = 5

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    
    stars = (n - i) * 2
    print("*" * stars, end="")
    
    for j in range(i, 0, -1):
        print(j, end="")
    
    print()