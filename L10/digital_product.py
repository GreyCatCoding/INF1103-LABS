from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self,product_id:str, name:str, price:float, stock:int ,supplier:Supplier, download_size:float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def display_information(self) -> None:
        """display information about the digital product"""
        super().display_information() # inherits display from Product class
        print(f"Download Size: {self.__download_size} MB")

    #property method allows access to download size without needing a separate getter method
    @property
    def download_size(self) -> float:
        """property for download size"""
        return self.__download_size
    
    def get_fulfilment_info(self) -> str:
        """return fulfilment information for the digital product"""
        return "This product is delivered digitally"
