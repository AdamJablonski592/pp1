def display_as_string(array):
    string = ""
    for item in array:
        if item == array[len(array)-1]:
            string += str(item)
        else:
            string += str(item)
            string += ","
        
    return string
nums = [5, 4, 3, 2, 6, 1]
print(f"String: {display_as_string(nums)}")