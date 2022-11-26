nums = [5, 11, 153, 2, 12]
def minmax(array):
    max_num = max(array)
    min_num = min(array)
    minmax = []
    minmax.append(min_num)
    minmax.append(max_num)
    return minmax
    
print(minmax(nums))