colors = ["red", "blue", "green"]

file = open("file.txt", "w")
for i in range(0, len(colors)):
    file.write(str(colors[i]))
    file.write("\n")
    
file.close()