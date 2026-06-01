METADATA = {
    "id": 901,
    "name": "Online Stock Span",
    "slug": "online-stock-span",
    "category": "Design",
    "aliases": [],
    "tags": ["monotonic_stack", "design", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(1) amortized",
    "space_complexity": "O(n)",
    "description": "Design an algorithm that collects daily price quotes for a stock and returns the span of that stock's price for the current day.",
}

class StockSpanner:
    """
    A class to calculate the span of a stock's price.
    
    The span is defined as the maximum number of consecutive days (starting from 
    the current day and going backward) for which the price was less than or 
    equal to the current price.
    """

    def __init__(self) -> None:
        """
        Initializes the StockSpanner with an empty monotonic stack.
        The stack stores tuples of (price, span).
        """
        # The stack will store pairs: (price, span_of_that_price)
        # This allows us to skip over elements that are smaller than the current price
        # by adding their pre-calculated spans to the current span.
        self.stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        """
        Calculates the span of the stock for the given price.

        Args:
            price: The current day's stock price.

        Returns:
            The span of the stock price for the current day.

        Examples:
            >>> spanner = StockSpanner()
            >>> spanner.next(100)
            1
            >>> spanner.next(80)
            1
            >>> spanner.next(60)
            1
            >>> spanner.next(70)
            2
            >>> spanner.next(60)
            1
            >>> spanner.next(75)
            4
            >>> spanner.next(85)
            6
        """
        current_span = 1
        
        # Use a monotonic decreasing stack approach.
        # While the stack is not empty and the top price is less than or equal 
        # to the current price, we "absorb" the span of the previous price.
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            current_span += prev_span
            
        # Push the current price and its total calculated span onto the stack.
        self.stack.append((price, current_span))
        
        return current_span

def solve() -> None:
    """
    Example usage of the StockSpanner class.
    """
    spanner = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    expected = [1, 1, 1, 2, 1, 4, 6]
    
    results = []
    for p in prices:
        results.append(spanner.next(p))
        
    assert results == expected
    print(f"Input: {prices}")
    print(f"Output: {results}")
    print("Test Passed!")
