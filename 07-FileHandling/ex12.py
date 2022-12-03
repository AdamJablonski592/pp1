f = open('shopping.txt', 'a')
product = input("Add a product: ")
f.writelines([product, "\n"])
f.close()