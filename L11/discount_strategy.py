from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    # DiscountStrategy guarantees every discount has an apply() method. 
    # The type hint documents that it should take and return a float. 
    """Abstract base for all order discounts. Each discount is its own class (Strategy pattern)."""

    @abstractmethod
    def apply(self, total: float) -> float:
        """Take an order total and return the discounted total."""
        pass
