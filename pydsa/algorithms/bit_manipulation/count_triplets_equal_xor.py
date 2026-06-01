METADATA = {
    "id": 1442,
    "name": "Count Triplets That Can Form Two Arrays of Equal XOR",
    "slug": "count-triplets-that-can-form-two-arrays-of-equal-xor",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "prefix_sum", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of triplets (i, j, k) such that the XOR sum of elements from i to j-1 equals the XOR sum of elements from j to k.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of triplets (i, j, k) such that 0 <= i < j < k < len(nums)
    and the XOR sum of nums[i...j-1] equals the XOR sum of nums[j...k].

    The condition XOR(i, j-1) == XOR(j, k) is mathematically equivalent to 
    XOR(i, k) == 0, because if A ^ B = 0, then A = B.

    Args:
        nums: A list of integers.

    Returns:
        The total count of valid triplets.

    Examples:
        >>> solve([1, 1, 2, 1, 1, 2])
        6
        >>> solve([0, 0, 0])
        1
    """
    n = len(nums)
    count = 0

    # We iterate through all possible starting points i
    for i in range(n):
        current_xor_sum = 0
        # We iterate through all possible ending points k
        # We need at least one element between i and k to form a valid j
        # So k must be at least i + 2
        for k in range(i, n):
            current_xor_sum ^= nums[k]
            
            # If the XOR sum from i to k is 0, any j between i and k 
            # (i < j < k) will satisfy the condition.
            # There are (k - i - 1) such possible values for j.
            if current_xor_sum == 0 and k >= i + 2:
                count += (k - i - 1)

    return count
