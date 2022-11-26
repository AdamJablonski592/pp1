nums = [12, 6, 4, 9, 3]

def star(n):
    return ("*" * n)
        
for num in nums:
    print(f"{num}: {star(num)}")