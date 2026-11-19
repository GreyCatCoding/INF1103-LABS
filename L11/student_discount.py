from discount_strategy import DiscountStrategy

class StudentDiscount(DiscountStrategy):
    """Fixed 5% discount for student orders."""

    def __init__(self) -> None:
        # The student rate is a fixed business rule, so callers do not pass it in.
        self.__percentage: float = 5.0

    def apply(self, total: float) -> float:
        """Apply the fixed 5% student discount to the total."""
        return total * (1 - self.__percentage / 100)