with open('text_file.txt', 'r') as f1:
    f1_content = f1.readlines()
    
with open('copy.text', 'w') as f2:
    for line in f1_content:
        f2.writelines(line)