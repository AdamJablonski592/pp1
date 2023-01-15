class C():
    
    def __init__(self, arr):
        self.arr = arr
        self.str = ""
    def __str__(self):
        for item in self.arr:
            self.str += str(item)
            self.str += "+"
        return self.str

print(C([5,12]))