input = input("Enter score: ")

try:
    score = float(input)

    if score < 0.0 or score > 1.0:
        print("Bad score")
    else:
        if score >= 0.9:
            print("A")
        elif score < 0.9 or score >= 0.8:
            print("B")
        elif score < 0.8 or score >= 0.7:
            print("C")
        elif score < 0.7 or score >= 0.6:
            print("D")
        else:
            print("F")

except:
    print("Bad score")