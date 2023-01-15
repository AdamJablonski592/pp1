def f(array2D):
    
    sum_arr = []
    for i in range(0, len(array2D[0])):
        sum_arr.append(0)
        
    for item in array2D:
        for i in range(0, len(item)):
            sum_arr[i] += item[i]
    
    print(sum_arr)
    
    
    
print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) )