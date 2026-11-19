from discount_strategy import DiscountStrategy


class PercentageDiscount(DiscountStrategy):
  
    def __init__(self, percentage: float) -> None:
        if percentage <= 0 or percentage >= 100:
            # 0 and 100 not allowed as 0 is no discount and 100 is full discount
            raise ValueError("Percentage must be greater than 0 and less than 100.")
    
        self.__percentage: float = percentage

    def apply(self, total: float) -> float:
        """Apply the percentage discount to the total"""
        return total * (1 - self.__percentage / 100)

    
