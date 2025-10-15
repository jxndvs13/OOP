import pickle
class Product:
    def __init__(self):
        self.pid = ""
        self.pname = ""
        self.price = 0.0
        self.description = ""
    def get_product_details(self):
        n_id = input("Enter Product ID: ")
        n_name = input("Enter Product Name: ")
        n_price = input("Enter Product Price: ")
        n_description = input("Enter Product Description: ")
        self.pid = n_id
        self.pname = n_name
        self.price = n_price
        self.description = n_description
        print("Product Updated")
    def display_product_info(self):
        print("ID:",self.pid)
        print(self.pname)
        print(self.description)
        print(self.price)
new_product = 0
newID = "0"
#main code
while True:
    print("")
    print("1. Create new product")
    print("2. Collect product details")
    print("3. Display the product")
    print("4. Write product to file")
    print("5. Read from file")
    print("6. Do 1, 2, and 4")
    print("0. Exit")
    op = input("Select Operation: ")
    print("")

    if op == "1":
        new_product = Product()
        newID = new_product.pid
        print("Product created")
    elif op == "2":
        Product.get_product_details(new_product)
    elif op == "3":
        Product.display_product_info(new_product)
    elif op == "4":
        f1 = open("inventory.dat","ab")
        pickle.dump(new_product, f1)
        f1.close()
    elif op == "5":
        f2 = open("inventory.dat","rb")
        while True:
            try:
                data = pickle.load(f2)
                data.display_product_info()
                print("")
            except EOFError:
                break
        f2.close()
    elif op == "6":
        new_product = Product()
        newID = new_product.pid
        Product.get_product_details(new_product)
        f1 = open("inventory.dat","ab")
        pickle.dump(new_product, f1)
        f1.close()
    elif op == "0":
        break
    else:
        print("Invalid input")