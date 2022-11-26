nums = [1, 52, 2, 3, 67, 13]
even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)