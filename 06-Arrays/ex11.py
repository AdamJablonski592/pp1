def compare (array1, array2):
    print(array1)
    print(array2)
    if len(array1) == len(array2):
        for i in range(0, len(array1)):
            if array1[i] == array2[i]:
                is_same = True
                continue
            else:
                is_same = False

        if is_same == True:
            print("The same")
        else:
            print("Not the same")
            
    else:
        print("Not the same")
        
array1 = ["True", "asfafsfas"]
array2 = ["True", "False"]

compare(array1, array2)