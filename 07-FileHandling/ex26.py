import re

with open('text_file.txt', 'r') as f:
    f_content = f.read()
    words = re.findall('\w{6,}', f_content)
    for item in words:
        print(item)