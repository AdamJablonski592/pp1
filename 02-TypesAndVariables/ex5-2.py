prompt = input("Enter a number:")

num_sum = 0
num_count = 1
num_list = []
num_min = 0
num_mix = 0

try:
    num_sum += float(prompt)
    num_list.append(num_sum)
except:
    print("Invalid input")

while prompt != 'done':
    try:
        prompt = input("Enter a number:")
        number = float(prompt)
        num_list.append(number)
        num_sum += number
        num_count += 1
    except:
        print("Invalid input")
        
if prompt == 'done':
    print(f"{num_sum} {num_count} {min(num_list)} {max(num_list)}")