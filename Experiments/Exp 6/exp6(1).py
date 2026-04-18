def find_max_min(lst):
    max_val = lst[0]
    min_val = lst[0]

    for x in lst:
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x

    return max_val, min_val

lst = list(map(int, input("Enter numbers: ").split()))
print(find_max_min(lst))