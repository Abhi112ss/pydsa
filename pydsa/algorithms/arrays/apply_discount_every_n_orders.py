METADATA = {
    "id": 1357,
    "name": "Apply Discount Every n Orders",
    "slug": "apply-discount-every-n-orders",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(N)",
    "description": "Design a system that applies a discount to every n-th purchase of a specific product.",
}

class DiscountService:
    """
    A service to manage product prices and apply discounts on every n-th purchase.
    """

    def __init__(self, prices: list[int], discount: int, n: int):
        """
        Initializes the service with product prices, discount amount, and frequency.

        Args:
            prices: A list of initial prices for each product.
            discount: The fixed amount to subtract from the price.
            n: The frequency of the discount (every n-th purchase).
        """
        # Store prices in a dictionary for O(1) access by product index
        self.product_prices = {i: price for i, price in enumerate(prices)}
        self.discount_amount = discount
        self.discount_frequency = n
        # Track the number of times each product has been purchased
        self.purchase_counts = {}

    def purchase(self, product_id: int) -> int:
        """
        Processes a purchase for a given product and returns the price paid.

        Args:
            product_id: The index of the product being purchased.

        Returns:
            The price paid after applying any applicable discount.

        Examples:
            >>> service = DiscountService([10, 20, 30], 5, 3)
            >>> service.purchase(0)
            10
            >>> service.purchase(0)
            10
            >>> service.purchase(0)
            5
        """
        # Increment the purchase count for the specific product
        current_count = self.purchase_counts.get(product_id, 0) + 1
        self.purchase_counts[product_id] = current_count

        base_price = self.product_prices[product_id]

        # Check if the current purchase count is a multiple of n
        if current_count % self.discount_frequency == 0:
            return base_price - self.discount_amount
        
        return base_price


def solve():
    """
    Entry point to demonstrate the functionality of the DiscountService.
    """
    # Example usage
    prices = [10, 20, 30]
    discount = 5
    n = 3
    
    service = DiscountService(prices, discount, n)
    
    # Test sequence
    results = []
    # Product 0 purchased 3 times (discount on 3rd)
    results.append(service.purchase(0)) # 10
    results.append(service.purchase(0)) # 10
    results.append(service.purchase(0)) # 5
    
    # Product 1 purchased 1 time
    results.append(service.purchase(1)) # 20
    
    # Product 0 purchased 3 more times (discount on 6th)
    results.append(service.purchase(0)) # 10
    results.append(service.purchase(0)) # 10
    results.append(service.purchase(0)) # 5
    
    return results
