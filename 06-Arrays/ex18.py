nums = [1, 632, 2, 55, 3, 12]

def bubblesort(array):
    n = len(array)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swapped:
            return
        
bubblesort(nums)
print(nums)