try:
    num = int(input("Enter a number: "))
    print(num**2)
except (KeyboardInterrupt):
    print("\nYou should have entered a number.... Program Termination.....")
except ValueError:
    print("Please check before you enter..... Program Termination.....")
print("Bye")