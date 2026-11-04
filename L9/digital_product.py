from product import Product

class DigitalProduct(Product):
    def __init__(self,product_id, name, price, stock , download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        """display information about the digital product"""
        super().display_information() # inherits display from Product class
        print(f"Download Size: {self.__download_size} MB")

    def get_download_size(self):
        """getter for download size"""
        return self.__download_size

    def get_fulfilment_info(self):
        return "This product is delivered digitally"
