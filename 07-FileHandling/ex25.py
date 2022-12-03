import re

message = "To be, or not to be, that is the question"
words = re.findall("\w+", message)
counter = 0
for item in words:
    counter += 1
    
print(counter)