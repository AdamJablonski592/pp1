nums = [15, 8, 31, 47, 2, 19]

def reverse(array):
    reverse_array = []
    for i in range(len(nums) - 1, -1, -1):
        reverse_array.append(nums[i])
    return reverse_array

print(reverse(nums))