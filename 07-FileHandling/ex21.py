with open('num_pow.txt', 'w') as f:
    for i in range(1,11):
        str_i = str(i)
        s_i = str(i**2)
        t_i = str(i**3)
        
        num_arr = [str_i, ",", s_i, ",", t_i]
        if i == 10:
            f.writelines(num_arr)
        else:
            f.writelines(num_arr)
            f.write("\n")