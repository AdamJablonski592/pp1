import re

def f(first_letter, last_letter):
    amount = 0
    with open('test.txt', 'r', encoding="utf-8") as f:
        text = f.read()
        for line in text.split():
            new_string = line.replace(',','').replace('.','').replace('!','')
            newer_string = new_string.replace('?','').replace(';','').replace('"',' ')
            newererer_string = newer_string.strip()
            if newererer_string[0] == first_letter and newererer_string[-1] == last_letter:
                amount += 1
            
        print(amount)
            
            
f("w", "d")