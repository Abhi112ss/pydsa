METADATA = {
    "id": 1814,
    "name": "Count Nice Pairs in an Array",
    "slug": "count-nice-pairs-in-an-array",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count pairs (i, j) such that nums[i] + nums[j] is divisible by nums[i] - nums[j].",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of nice pairs in the array.
    
    A pair (i, j) is nice if (nums[i] + nums[j]) % (nums[i] - nums[j]) == 0.
    This condition is mathematically equivalent to (nums[i] - nums[j]) % k == 0,
    which can be rewritten as nums[i] % k == nums[j] % k.

    Args:
        nums: A list of integers.
        k: The divisor constant.

    Returns:
        The total number of nice pairs.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 1)
        10
        >>> solve([1, 2, 3, 4, 5], 2)
        3
    """
    MOD = 10**9 + 7
    remainder_counts: dict[int, int] = {}
    nice_pairs_count = 0

    for num in nums:
        # Calculate the remainder of the current number when divided by k
        remainder = num % k
        
        # If this remainder has been seen before, every previous occurrence 
        # forms a 'nice pair' with the current number.
        if remainder in remainder_counts:
            nice_pairs_count = (nice_pairs_count + remainder_counts[remainder]) % MOD
            remainder_counts[remainder] += 1
        else:
            remainder_counts[remainder] = 1

    return nice_pairs_count
