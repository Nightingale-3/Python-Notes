try:
    print("Raising an exception...")
    raise ValueError
finally:
    print("Performing clean up in Finally.....")
    