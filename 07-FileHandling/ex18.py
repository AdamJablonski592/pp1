with open('GrainsAndBread.txt', 'r') as f1:
    f1_content = f1.readlines()
    
with open('MeatAndFish.txt', 'r') as f2:
    f2_content = f2.readlines()
    
with open('shoppinglist.txt', 'w') as f3:
    f3.writelines(f1_content)
    f3.writelines(f2_content)