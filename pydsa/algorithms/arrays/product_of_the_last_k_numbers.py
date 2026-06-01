METADATA = {
    "id": 1352,
    "name": "Product of the Last K Numbers",
    "slug": "product_of_the_last_k_numbers",
    "category": "Design",
    "aliases": [],
    "tags": ["prefix_sum", "design", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a class that supports adding an integer and calculating the product of the last k numbers.",
}

class ProductOfLastKNumbers:
    def __init__(self) -> None:
        """
        Initializes the data structure.
        We use a prefix product list to allow O(1) product calculation.
        We also track the index of the last zero encountered to handle zero-product cases.
        """
        self.prefix_products: list[float] = [1.0]
        self.last_zero_index: int = -1

    def add(self, val: int) -> None:
        """
        Adds an integer to the sequence.

        Args:
            val: The integer to add.
        """
        if val == 0:
            # If zero is added, all products involving this index will be zero.
            # We reset the prefix product list and update the last zero index.
            self.prefix_products = [1.0]
            self.last_zero_index = len(self.prefix_products) + 0 # Logic handled by resetting list
            # To keep it simple and O(1) amortized, we reset the list.
            # The 'last_zero_index' effectively marks the boundary of the current non-zero segment.
            self.last_zero_index = 0 
            # Actually, a cleaner way to handle the 'reset' is to just clear the list 
            # and treat the current position as the new start.
            self.prefix_products = [1.0]
            self.last_zero_index = 0
        else:
            # Multiply the last prefix product by the new value.
            self.prefix_products.append(self.prefix_products[-1] * val)

    def find_product(self, k: int) -> float:
        """
        Returns the product of the last k numbers.

        Args:
            k: The number of elements to multiply.

        Returns:
            The product of the last k numbers.

        Examples:
            >>> obj = ProductOfLastKNumbers()
            >>> obj.add(3)
            >>> obj.add(2)
            >>> obj.add(5)
            >>> obj.find_product(2)
            10.0
            >>> obj.add(0)
            >>> obj.find_product(3)
            0.0
        """
        # If k is greater than or equal to the number of elements since the last zero,
        # it means a zero was included in the last k elements.
        if k >= len(self.prefix_products):
            return 0.0
        
        # Otherwise, use the prefix product formula: product(last k) = prefix[end] / prefix[end - k]
        # This works because prefix_products[i] = val[0] * ... * val[i-1]
        return self.prefix_products[-1] / self.prefix_products[-k - 1]

def solve():
    """
    Example usage of the ProductOfLastKNumbers class.
    """
    obj = ProductOfLastKNumbers()
    obj.add(3)
    obj.add(2)
    obj.add(5)
    print(obj.find_product(2))  # Expected: 10.0
    obj.add(0)
    print(obj.find_product(3))  # Expected: 0.0
