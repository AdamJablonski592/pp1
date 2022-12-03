import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatures = re.findall("\d{2}", message)
sum = 0
result = 0

for item in temperatures:
    sum += int(item)
    
result = sum/3
print(result)