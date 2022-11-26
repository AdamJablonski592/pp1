nums1 = [4, 36, 12, 28, 9, 44, 5]
nums2 = [5, 1, 36]

for num in nums1:
    if num not in nums2:
        print(num, end=" ")
    else:
        continue