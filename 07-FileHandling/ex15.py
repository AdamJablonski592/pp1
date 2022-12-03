with open('text_file.txt', 'r') as f:
    file_lines = f.readlines()
    counter = 0
    i = 0
    while counter < 5:
        print(file_lines[i])
        counter += 1
        i += 1
        
        if counter == 5:
            input("Press enter to continue")
            counter = 0
            
        if i == 29:
            break
            