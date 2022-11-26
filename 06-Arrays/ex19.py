nums = [1, 51, 22, 1, 3, 4]

for num in nums:
    if nums.count(num) > 1:
        continue
    else:
        print(num)