METADATA = {
    "id": 2364,
    "name": "Count Number of Bad Pairs",
    "slug": "count-number-of-bad-pairs",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count pairs (i, j) such that i < j and j - i != nums[j] - nums[i].",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of bad pairs in an array.
    
    A pair (i, j) is bad if i < j and j - i != nums[j] - nums[i].
    This is equivalent to saying a pair is good if nums[j] - j == nums[i] - i.
    The total number of pairs is n * (n - 1) / 2.
    We subtract the number of good pairs from the total pairs to get bad pairs.

    Args:
        nums: A list of integers.

    Returns:
        The total count of bad pairs.

    Examples:
        >>> solve([4, 1, 3, 3])
        2
        >>> solve([1, 1, 1, 1, 1])
        0
        >>> solve([1, 2, 3, 4])
        0
    """
    n = len(nums)
    # Total possible pairs (i, j) where i < j
    total_pairs = n * (n - 1) // 2
    
    # A pair is 'good' if nums[j] - j == nums[i] - i.
    # We use a hash map to store the frequency of the value (nums[i] - i).
    diff_counts: dict[int, int] = {}
    good_pairs = 0
    
    for index, value in enumerate(nums):
        # Calculate the transformation value that defines a 'good' relationship
        transformed_val = value - index
        
        # If this transformed value has been seen before, every previous occurrence
        # forms a 'good' pair with the current index.
        if transformed_val in diff_counts:
            good_pairs += diff_counts[transformed_val]
            diff_counts[transformed_val] += 1
        else:
            diff_counts[transformed_val] = 1
            
    # Bad pairs = Total pairs - Good pairs
    return total_pairs - good_pairs
