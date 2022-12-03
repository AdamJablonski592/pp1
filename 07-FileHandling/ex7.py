f = open('countries.txt', 'r')
f_content = f.readlines()
counter = 1

for line in f_content:
    print(f"{counter}: {line}")
    counter += 1

f.close()