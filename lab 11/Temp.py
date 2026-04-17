c = int(input("Enter the temperature in Celsius: "))
f = (c * 9/5) + 32
assert(f<=32), "Its freezing"
print(f"The temperature in Fahrenheit = {f}")