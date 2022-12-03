with open('text_file.txt', 'r') as f1:
    f1_content = f1.read()
    
with open('copy.text', 'w') as f2:
    f2.writelines(f1_content)