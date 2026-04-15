def Divide(num, den):
    try:
        quo = num / den
    except ZeroDivisionError:
        print("You cannot divide by zero.... Program Terminating...")

Divide(10, 0)