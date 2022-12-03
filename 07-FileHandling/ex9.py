f = open('numbers.txt', 'r')
f_lines = f.readlines()
sum = 0
for line in f_lines:
    sum += int(line)
    
print(sum)
f.close()