import random
class Arrays():

    @staticmethod
    def create_array(num_of_elem, val_of_elem):
        array = []
        for i in range(0, num_of_elem):
            array.append(val_of_elem)
        return array

    @staticmethod
    def create_array_rand(num_of_elem, min_val, max_val):
        array = []
        for i in range(0, num_of_elem):
            array.append(random.randint(min_val, max_val))
        return array

    @staticmethod
    def num_in_range(array, val_from, val_to):
        counter = 0
        for item in array:
            if item >= val_from and item <= val_to:
                counter += 1
        return counter

new_arr = Arrays.create_array(10, 4)
print(new_arr)

newer_arr = Arrays.create_array_rand(20, -7, 8)
print(newer_arr)

num_of_val = Arrays.num_in_range(newer_arr, -1, 1)
print(num_of_val)