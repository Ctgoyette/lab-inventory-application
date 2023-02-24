class Item:
    def __init__(self, name, brand = None, quantity = None, description = None, location = None):
        self.item_name = name
        self.item_brand = brand
        self.item_quantity = quantity
        self.item_description = description
        self.item_location = location

    def get_name(self):
        return self.item_name

    def get_brand(self):
        return self.item_brand

    def get_quantity(self):
        return self.item_quantity

    def get_description(self):
        return self.item_description
    
    def get_location(self):
        return self.item_location


    def set_name(self, name):
        self.item_name = name

    def set_brand(self, brand):
        self.item_brand = brand

    def set_quantity(self, quantity):
        self.item_quantity = quantity

    def set_description(self, description):
        self.item_description = description

    def set_location(self, location):
        self.item_location = location

    
    name = property(fget = get_name, fset = set_name, doc = 'Name of item')
    brand = property(fget = get_brand, fset = set_brand, doc = 'Brand of item')
    quantity = property(fget = get_quantity, fset = set_quantity, doc = 'Number of items in system')
    description = property(fget = get_description, fset = set_description, doc = 'Description of the item')
    location = property(fget = get_location, fset = set_location, doc = 'Location of the item in the lab')