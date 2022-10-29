def letter_checker(string, letter):
    counter = 0
    for lettr in string:
        if lettr ==  letter:
            counter += 1
        else:
            continue
    return counter

result = letter_checker("You never get a second chance to make a first impression", "e")
print(result)