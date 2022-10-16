prompt = input("Enter a number:")

num_sum = 0
num_count = 1
num_avg = 0

try:
    num_sum += float(prompt)
except:
    print("Invalid input")

while prompt != 'done':
    try:
        prompt = input("Enter a number:")
        number = float(prompt)
        num_sum += number
        num_count += 1
    except:
        print("Invalid input")
        
if prompt == 'done':
    num_avg = num_sum/num_count
    print(f"{num_sum} {num_count} {num_avg}")