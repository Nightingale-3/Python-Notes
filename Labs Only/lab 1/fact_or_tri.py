def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * fact(n - 1)
    
n = int(input("Enter the value of n: "))
print("Factorial of", n, "is", fact(n))