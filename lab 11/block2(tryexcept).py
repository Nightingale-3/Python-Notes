try:
    num = int(input("Enter a number: "))
    print(num**2)
except (KeyboardInterrupt, ValueError, TypeError):
    print("Please check before you enter..... Program Terminating.....")
print("Bye")