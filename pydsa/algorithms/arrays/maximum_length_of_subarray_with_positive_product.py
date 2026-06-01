METADATA = {
    "id": 1567,
    "name": "Maximum Length of Subarray With Positive Product",
    "slug": "maximum-length-of-subarray-with-positive-product",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a subarray with a positive product.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum length of a subarray with a positive product.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest subarray with a positive product.

    Examples:
        >>> solve([1, -2, -3, 4])
        4
        >>> solve([0, 1, -2, -3, -4])
        3
        >>> solve([-1, -2, -3, 0, 1])
        2
    """
    max_len = 0
    # pos_len tracks the length of the current subarray with a positive product
    pos_len = 0
    # neg_len tracks the length of the current subarray with a negative product
    neg_len = 0

    for num in nums:
        if num > 0:
            # Positive number increases positive length
            pos_len += 1
            # If we had a negative product, it stays negative but grows in length
            if neg_len > 0:
                neg_len += 1
            else:
                neg_len = 0
        elif num < 0:
            # Negative number swaps the roles of positive and negative lengths
            # New positive length comes from previous negative length + 1
            # New negative length comes from previous positive length + 1
            new_pos_len = neg_len + 1 if neg_len > 0 else 0
            new_neg_len = pos_len + 1
            pos_len = new_pos_len
            neg_len = new_neg_len
        else:
            # Zero resets both counters as any subarray containing zero has product 0
            pos_len = 0
            neg_len = 0
        
        # Update the global maximum with the current positive length
        if pos_len > max_len:
            max_len = pos_len

    return max_len
