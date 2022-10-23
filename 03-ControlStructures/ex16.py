n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

nums = []
nums.append(n1)
nums.append(n2)

print(f"Numbers in ascending order: {min(nums)}, {max(nums)}")