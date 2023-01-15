def f(d):
    cars_in = []
    for item in d:
        if item[1] == 'in':
            cars_in.append(item[0])
        elif item[1] == 'out':
            cars_in.remove(item[0])
    cars_in.sort()
    print(cars_in)
    
    
cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]

f(cars)