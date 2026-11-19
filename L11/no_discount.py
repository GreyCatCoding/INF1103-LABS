from discount_strategy import DiscountStrategy


class NoDiscount(DiscountStrategy):
    """Default strategy: leaves the order total unchanged."""

    def apply(self, total: float) -> float:
        """Return the total exactly as given."""
        return total
