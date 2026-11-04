from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    """Interface for products that can be shipped physically."""

    @abstractmethod
    def calculate_shipping_cost(self):
        """Calculate the shipping cost for the product"""
        pass
