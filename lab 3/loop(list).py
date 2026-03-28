fruits = ["apple", "banana", "cherr"]
for x in fruits:
    print(x)

    for x in "banana":
        print(x)

        fruit = ["apple", "banana", "cherr"]
        for x in fruits:
            print(x)
            if x == "banana":
                break
        
            for x in fruit:
                if x == "banana":
                    break
                print(x)