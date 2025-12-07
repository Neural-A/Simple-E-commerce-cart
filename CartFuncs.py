class CartFunctions():

    def __init__(self):
        super().__init__()
        self.items =  {}

    def add_to_cart(self,itemName,price):

        if itemName != self.items:
            self.items[itemName] = {"Price: ":price}
    def __repr__(self):
        return str(self.items)

    def removing(self,item):
        if item in self.items:
            del self.items[item]
        else:
            print("ERROR: ITEM NOT FOUND")
        return self.items
