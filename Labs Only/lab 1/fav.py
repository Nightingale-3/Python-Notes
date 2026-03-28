def func(name, *fav_subjects):
    print("\n",name, "likes to read ")
    for subject in fav_subjects:
        print(subject)

func("Gouransh", "Mathematics", "Android programming")
func("Risha", "C", "Data Structures", "Design and Analysis of Algorithms")
func("Krish")