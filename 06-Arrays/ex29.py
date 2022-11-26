nums1 = [1, 5, 4]
nums2 = [1, 5, 4, 2, 21, 321]

for num in nums1:
    if num in nums2:
        is_subset = True
    else:
        is_subset = False
        
print(is_subset)