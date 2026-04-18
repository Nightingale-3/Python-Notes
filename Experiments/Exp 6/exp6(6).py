lst = list(map(int, input("Enter numbers: ").split()))

f = lambda x: (max(x), min(x))

print(f(lst))