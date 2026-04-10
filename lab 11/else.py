try:
    file = pen("File1.txt")
    str = f.readline()
    print(str)
except IOError:
    print("Error occured during Input..... Program Terminating....")

else:
    print("Program terminating Successfully....")