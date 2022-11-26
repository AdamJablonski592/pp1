import math
nums1 = [1, 0, 9, 4, 6]
nums2 = [6, 8, 3, 1, 0, 5, 7]

def median(array):
    if len(array) % 2 == 0:
        lower_num = array[math.floor((len(array) / 2)-1)]
        higher_num = array[math.floor(len(array) / 2)]
        med = (lower_num + higher_num) / 2
        return med
    else:
        med = array[math.floor(len(array) / 2)]
        return med
        
print(median(nums2))