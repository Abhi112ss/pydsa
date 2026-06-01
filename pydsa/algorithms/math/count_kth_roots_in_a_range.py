METADATA = {
    "id": 3932,
    "name": "Count K-th Roots in a Range",
    "slug": "count_kth_roots_in_a_range",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(log(max_val))",
    "space_complexity": "O(1)",
    "description": "Count how many integers x exist such that x^k falls within the range [left, right].",
}

def solve(left: int, right: int, k: int) -> int:
    """
    Counts the number of integers x such that left <= x^k <= right.

    Args:
        left: The lower bound of the range (inclusive).
        right: The upper bound of the range (inclusive).
        k: The exponent used to calculate the k-th root.

    Returns:
        The count of integers x whose k-th power is in [left, right].

    Examples:
        >>> solve(1, 10, 2)
        3  # 1^2=1, 2^2=4, 3^2=9 are in [1, 10]
        >>> solve(10, 20, 2)
        1  # 4^2=16 is in [10, 20]
    """
    if left > right:
        return 0

    def find_floor_root(target: int, exponent: int) -> int:
        """
        Finds the largest integer x such that x^exponent <= target.
        Uses binary search to handle potential precision issues with pow().
        """
        if target < 0:
            return 0 # Problem context implies non-negative integers
        if target == 0:
            return 0
        if target == 1:
            return 1
        
        low = 1
        # Upper bound for x is target^(1/k). 
        # For k >= 1, x is at most target.
        high = target
        # Optimization: for k >= 2, high can be much smaller, 
        # but target is a safe upper bound for binary search.
        # For very large target, we can use a tighter bound like 2**(log2(target)/k + 1)
        # but standard binary search is O(log(target)).
        
        # To prevent overflow in high-k scenarios, we cap high
        # if target is extremely large, but Python handles arbitrary size ints.
        # However, we can use a more efficient upper bound for high.
        if exponent >= 60: # 2^60 is very large
            high = 2
        elif exponent >= 2:
            high = int(target**(1/exponent)) + 2

        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                low = 1
                continue
                
            # Check mid^exponent <= target without causing massive slowdowns
            # Python handles large ints, so mid**exponent is safe.
            try:
                val = pow(mid, exponent)
            except OverflowError:
                # This shouldn't happen with Python's arbitrary precision
                val = target + 1
                
            if val <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    # The number of integers x such that x^k <= right is find_floor_root(right, k)
    # The number of integers x such that x^k < left is find_floor_root(left - 1, k)
    # The count in [left, right] is the difference.
    
    upper_count = find_floor_root(right, k)
    lower_count = find_floor_root(left - 1, k)
    
    return max(0, upper_count - lower_count)
