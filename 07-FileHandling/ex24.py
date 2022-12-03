import re

message = "To be, or not to be, that is the question"
vowels = re.findall("[aeiouy]", message)
count = 0
for item in vowels:
    count += 1
    
print(count)