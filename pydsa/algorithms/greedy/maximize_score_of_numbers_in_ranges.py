METADATA = {
    "id": 3281,
    "name": "Maximize Score of Numbers in Ranges",
    "slug": "maximize-score-of-numbers-in-ranges",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the total score by selecting non-overlapping ranges where each range's score is the product of its elements.",
}

def solve(nums: list[int], ranges: list[list[int]]) -> int:
    """
    Calculates the maximum score by selecting non-overlapping ranges.
    
    The score of a range is the product of all elements within that range.
    Since we want to maximize the score and all elements are positive, 
    we treat each range as an interval with a specific weight (its product).
    This is a variation of the Weighted Interval Scheduling problem.

    Args:
        nums: A list of integers.
        ranges: A list of ranges, where each range is [start, end] (1-indexed).

    Returns:
        The maximum possible score.

    Examples:
        >>> solve([1, 2, 3, 4], [[1, 2], [3, 4]])
        24
        >>> solve([1, 1, 1, 1], [[1, 1], [2, 2], [3, 3], [4, 4]])
        4
    """
    MOD = 10**9 + 7
    
    # Precompute prefix products to calculate range products in O(1)
    # Since we need to handle potential large numbers, we use the product directly.
    # Note: The problem constraints usually imply products can be very large,
    # but Python handles arbitrary precision integers automatically.
    n = len(nums)
    prefix_products = [1] * (n + 1)
    for i in range(n):
        prefix_products[i + 1] = prefix_products[i] * nums[i]

    # Transform ranges into (start, end, score) tuples
    # Convert 1-based indexing to 0-based indexing
    processed_ranges = []
    for start, end in ranges:
        # range [start, end] 1-indexed is [start-1, end-1] 0-indexed
        # Product of nums[i] for i in [s-1, e-1] is prefix[e] / prefix[s-1]
        # However, division is risky with large numbers; we use the prefix array directly.
        # But since we need to maximize, we calculate the actual product.
        s_idx = start - 1
        e_idx = end - 1
        
        # Calculate product for the range
        current_product = 1
        for i in range(s_idx, e_idx + 1):
            current_product *= nums[i]
        
        processed_ranges.append((s_idx, e_idx, current_product))

    # Sort ranges by their end positions to apply Dynamic Programming
    processed_ranges.sort(key=lambda x: x[1])

    # dp[i] will store the maximum score using a subset of the first i sorted ranges
    # We use a list of (end_index, max_score) to perform binary search
    # dp_table stores (end_position, max_score_up_to_this_end_position)
    dp_table = [(-1, 0)]  # Base case: end position -1, score 0

    for start, end, score in processed_ranges:
        # Find the latest range that ends before the current range starts
        # We need the largest index 'idx' such that dp_table[idx].end < start
        
        # Binary search for the best previous non-overlapping range
        low = 0
        high = len(dp_table) - 1
        best_prev_score = 0
        
        while low <= high:
            mid = (low + high) // 2
            if dp_table[mid][0] < start:
                best_prev_score = dp_table[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        
        current_total_score = best_prev_score + score
        
        # If this range improves the score for its end position, add it to dp_table
        if current_total_score > dp_table[-1][1]:
            # If the end position is the same as the last entry, update it
            if dp_table[-1][0] == end:
                dp_table[-1] = (end, current_total_score)
            else:
                dp_table.append((end, current_total_score))

    return dp_table[-1][1] % MOD
