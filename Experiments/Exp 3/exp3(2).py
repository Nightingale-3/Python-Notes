n = int(input("Enter number: "))
temp = n
sum = 0
digits = len(str(n))

while temp > 0:
    d = temp % 10
    sum += d ** digits
    temp //= 10

if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")