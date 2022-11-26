nums = [1, 5, 6, 9]
def sum(array):
    sums = 0
    for num in nums:
        sums += num
    return sums

def array2str(array):
    string = ""
    for item in nums:
        string += str(item)
        string += " "
    return string

print(sum(nums))
print(array2str(nums))