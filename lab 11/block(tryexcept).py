num = int(input("Enter the numerator: "))
deno = int(input("Enter the denominater: "))
try:
    quo = num/deno
    print("QUOTIENT: ", quo)
except ZeroDivisionError:
    print("Denominator cannot be zero.")