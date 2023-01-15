def f(dictionary, x, y):
    sum = 0
    
    for k, v in dictionary.items():
        for num in v:
            if num >= x and num <= y:
                sum += num

    return sum
        

f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10) 