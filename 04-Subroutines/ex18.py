def sum_of_digits(num):
    parsed_num = str(num)
    sum = 0
    for digit in parsed_num:
        sum += int(digit)
    
    return sum

result = sum_of_digits(7182)
print(result)