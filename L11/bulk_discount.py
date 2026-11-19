from discount_strategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:

        if threshold <= 0.0:
            raise ValueError("Threshold must be greater than 0.")
        
        if amount <= 0.0 or amount > threshold:

            raise ValueError("Amount must be greater than 0 and less than the threshold.")
        
        self.__threshold: float = threshold
        self.__amount: float = amount


    def apply(self, total: float) -> float:
        """Apply the bulk discount if the total meets the threshold."""
        if total >= self.__threshold:
            return total - self.__amount
        return total
        