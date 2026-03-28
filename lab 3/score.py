score = int(input("Enter the given score: "))

if score < 100 and score >= 90 :
    print("S Grade")
elif score < 90 and score >= 80 :
    print("A Grade")
elif score < 80 and score >= 70 :
    print("B Grade")
elif score < 70 and score >= 60 :
    print("C Grade")
elif score < 60 and score > 50 :
    print("D Grade")
elif score == 50:
    print("E Grade")
elif score < 50 and score >= 0 :
    print("U Grade")
else:
    print("Give a number b/w 0 and 100")