tasks = []

while True:
    print("\n1.Add 2.View 3.Remove 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        task = input("Enter task: ")
        tasks.append(task)

    elif ch == 2:
        print("Tasks:")
        for t in tasks:
            print("-", t)

    elif ch == 3:
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)

    else:
        break