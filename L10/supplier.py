class Supplier:
    """association: a supplier can be associated with multiple products"""
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        """initialize a supplier with id, name, and contact email"""
        self.__supplier_id : str = supplier_id
        self.__name : str= name
        self.__contact_email : str = contact_email

    @property
    def supplier_id(self) -> str:
        return self.__supplier_id

    @property
    def name(self) -> str:
        return self.__name


    # # take in the new value and set the private variable to the new value
    # @name.setter
    # def name(self,value:str) -> None:
    #     self.__name = value


    @property
    def contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        """display information about the supplier"""
        print(f"supplier id : {self.supplier_id}\n"
              f"name : {self.name}\n"
              f"contact_email: {self.contact_email}")

# if __name__ == "__main__":
#     supplier = Supplier("S001", "Acme Supplies", "sales@acme.com")
#     supplier.display_information()
#     print(supplier.name)
#     supplier.name = "Changed"
