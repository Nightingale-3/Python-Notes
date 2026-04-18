contacts = {}

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == 2:
        name = input("Enter name: ")
        print(contacts.get(name, "Not found"))

    elif ch == 3:
        name = input("Enter name: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
        else:
            print("Not found")

    elif ch == 4:
        name = input("Enter name: ")
        contacts.pop(name, None)

    else:
        break