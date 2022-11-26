nums = [1, 23, 5, 382, 1, 17, 4, 906]

print("-" * 41)
print("|", end="")
for num in nums:
    whitespace = 4
    print(" " * (whitespace - len(str(num))), end="")
    print(num, end="")
    print("|", end="")
print("\n", "-" * 41)