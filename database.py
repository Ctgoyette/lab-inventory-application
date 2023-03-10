from sheets_integration import Sheet
from categories import Category
from item_storage import Item

class Database:
    def __init__(self, sheet, credentials):
        self.categories = dict()
        self.contents_file = Sheet(sheet, credentials)
        self.load_database()

    def load_database(self):

        for category in self.contents_file.get_categories():

            new_category = Category(category)

            self.contents_file.select_worksheet(category)
            brand_values = self.contents_file.get_col_values('Brand')
            quantity_values = self.contents_file.get_col_values('# of Units')
            description_values = self.contents_file.get_col_values('Description')
            location_values = self.contents_file.get_col_values('Location')

            item_values = self.contents_file.get_col_values('Item')

            for item in item_values:

                item_row = item_values.index(item)
                brand = brand_values[item_row] if brand_values is not None else None
                quantity = quantity_values[item_row] if quantity_values is not None else None
                description = description_values[item_row] if description_values is not None else None
                location = location_values[item_row] if location_values is not None else None

                new_item = Item(item, brand, quantity, description, location)

                new_category.category_items[item] = new_item

            self.categories[category] = new_category
