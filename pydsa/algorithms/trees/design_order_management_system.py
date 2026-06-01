METADATA = {
    "id": 3822,
    "name": "Design Order Management System",
    "slug": "design_order_management_system",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "treemap", "balanced_bst", "data_structures"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a system to manage orders with support for adding, canceling, and retrieving orders within a specific price range.",
}

import bisect

class OrderManagementSystem:
    """
    A system to manage orders using a sorted list to simulate a TreeMap/Balanced BST.
    
    This implementation uses a sorted list of tuples (price, order_id) to maintain 
    orderings, allowing for efficient range queries via binary search.
    """

    def __init__(self):
        """Initializes the order management system."""
        # Stores (price, order_id) tuples sorted primarily by price, then order_id
        self.sorted_orders: list[tuple[float, int]] = []
        # Maps order_id to its current price for O(1) lookup during cancellation
        self.order_to_price: dict[int, float] = {}

    def add_order(self, order_id: int, price: float) -> None:
        """
        Adds a new order to the system.

        Args:
            order_id: Unique identifier for the order.
            price: The price of the order.

        Examples:
            >>> oms = OrderManagementSystem()
            >>> oms.add_order(1, 100.0)
        """
        self.order_to_price[order_id] = price
        # Maintain sorted order: O(n) in worst case for list insertion, 
        # but O(log n) for finding the position. 
        # In a production environment with a true Balanced BST, this would be O(log n).
        bisect.insort(self.sorted_orders, (price, order_id))

    def cancel_order(self, order_id: int) -> bool:
        """
        Cancels an existing order.

        Args:
            order_id: The ID of the order to cancel.

        Returns:
            True if the order was successfully canceled, False otherwise.

        Examples:
            >>> oms = OrderManagementSystem()
            >>> oms.add_order(1, 100.0)
            >>> oms.cancel_order(1)
            True
            >>> oms.cancel_order(2)
            False
        """
        if order_id not in self.order_to_price:
            return False
        
        price = self.order_to_price.pop(order_id)
        # Find the specific (price, order_id) tuple to remove
        # Using bisect_left to find the index in O(log n)
        idx = bisect.bisect_left(self.sorted_orders, (price, order_id))
        
        # Verify the element at idx is indeed our target
        if idx < len(self.sorted_orders) and self.sorted_orders[idx] == (price, order_id):
            self.sorted_orders.pop(idx)
            return True
        return False

    def get_orders_in_range(self, min_price: float, max_price: float) -> list[int]:
        """
        Retrieves all order IDs within a given price range [min_price, max_price].
        Orders are returned sorted by price, then by order_id.

        Args:
            min_price: The lower bound of the price range (inclusive).
            max_price: The upper bound of the price range (inclusive).

        Returns:
            A list of order IDs within the specified range.

        Examples:
            >>> oms = OrderManagementSystem()
            >>> oms.add_order(1, 10.0)
            >>> oms.add_order(2, 20.0)
            >>> oms.add_order(3, 30.0)
            >>> oms.get_orders_in_range(15.0, 35.0)
            [2, 3]
        """
        # Find the starting index using binary search: O(log n)
        # We use a very small order_id (float('-inf')) to ensure we catch the min_price
        start_idx = bisect.bisect_left(self.sorted_orders, (min_price, float('-inf')))
        
        # Find the ending index: O(log n)
        # We use a very large order_id (float('inf')) to ensure we catch the max_price
        end_idx = bisect.bisect_right(self.sorted_orders, (max_price, float('inf')))
        
        # Extract order IDs from the identified range: O(k) where k is number of orders in range
        return [order[1] for order in self.sorted_orders[start_idx:end_idx]]

def solve():
    """
    Test driver for the OrderManagementSystem.
    """
    oms = OrderManagementSystem()
    
    # Test Case 1: Basic Add and Range Query
    oms.add_order(1, 100.0)
    oms.add_order(2, 200.0)
    oms.add_order(3, 150.0)
    assert oms.get_orders_in_range(100.0, 150.0) == [1, 3]
    
    # Test Case 2: Cancellation
    assert oms.cancel_order(3) is True
    assert oms.cancel_order(99) is False # Non-existent
    assert oms.get_orders_in_range(100.0, 200.0) == [1, 2]
    
    # Test Case 3: Duplicate Prices
    oms.add_order(4, 150.0)
    oms.add_order(5, 150.0)
    # Should return [1, 4, 5, 2] if range is wide, but let's check specific range
    # Sorted order: (100.0, 1), (150.0, 4), (150.0, 5), (200.0, 2)
    assert oms.get_orders_in_range(150.0, 150.0) == [4, 5]
    
    print("All tests passed!")
