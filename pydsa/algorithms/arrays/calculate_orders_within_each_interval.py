METADATA = {
    "id": 2893,
    "name": "Calculate Orders Within Each Interval",
    "slug": "calculate-orders-within-each-interval",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting", "binary search", "prefix sum"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given an array of order timestamps and a list of intervals, return the number of orders falling within each interval.",
}

import bisect

def solve(orders: list[int], intervals: list[list[int]]) -> list[int]:
    """
    Calculates the number of orders that fall within each specified interval.

    An order is considered within an interval [start, end] if start <= order <= end.

    Args:
        orders: A list of integers representing the timestamps of orders.
        intervals: A list of lists, where each sub-list contains [start, end] 
            representing the interval boundaries.

    Returns:
        A list of integers where each element is the count of orders within 
        the corresponding interval.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [[1, 3], [2, 4], [6, 7]])
        [3, 3, 0]
        >>> solve([10, 20, 30], [[5, 15], [15, 25], [25, 35]])
        [1, 1, 1]
    """
    # Sort orders to enable efficient range queries via binary search
    sorted_orders = sorted(orders)
    results = []

    for start, end in intervals:
        # Find the first index where order >= start
        # bisect_left returns the leftmost insertion point to maintain order
        left_index = bisect.bisect_left(sorted_orders, start)
        
        # Find the first index where order > end
        # bisect_right returns the rightmost insertion point to maintain order
        right_index = bisect.bisect_right(sorted_orders, end)
        
        # The number of elements in the range [start, end] is the difference 
        # between the two indices
        count = right_index - left_index
        results.append(count)

    return results
