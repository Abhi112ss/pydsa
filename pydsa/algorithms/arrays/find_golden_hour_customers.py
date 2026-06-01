METADATA = {
    "id": 3705,
    "name": "Find Golden Hour Customers",
    "slug": "find_golden_hour_customers",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["sorting", "hash_map", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the number of customers whose purchase times fall within a specific golden hour interval.",
}

def solve(purchase_times: list[int], golden_hour_start: int, golden_hour_end: int) -> int:
    """
    Calculates the number of customers who made a purchase during the golden hour.

    Args:
        purchase_times: A list of integers representing the timestamps of purchases.
        golden_hour_start: The start timestamp of the golden hour (inclusive).
        golden_hour_end: The end timestamp of the golden hour (inclusive).

    Returns:
        The count of purchase timestamps that fall within [golden_hour_start, golden_hour_end].

    Examples:
        >>> solve([10, 20, 30, 40, 50], 15, 35)
        2
        >>> solve([1, 2, 3], 4, 5)
        0
    """
    # Sort the times to allow for efficient range searching via binary search
    # Although a simple linear scan is O(n), sorting allows for O(log n) queries 
    # if this were part of a larger system with multiple intervals.
    # For a single query, O(n) is sufficient, but we follow the O(n log n) requirement.
    sorted_times = sorted(purchase_times)
    n = len(sorted_times)
    
    def find_first_ge(target: int) -> int:
        """Finds the first index where sorted_times[i] >= target using binary search."""
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if sorted_times[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def find_first_gt(target: int) -> int:
        """Finds the first index where sorted_times[i] > target using binary search."""
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if sorted_times[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low

    # Find the range of indices that fall within [golden_hour_start, golden_hour_end]
    # start_idx is the first index where time >= golden_hour_start
    start_idx = find_first_ge(golden_hour_start)
    
    # end_idx is the first index where time > golden_hour_end
    end_idx = find_first_gt(golden_hour_end)

    # The number of elements in the range is the difference between indices
    return max(0, end_idx - start_idx)
