METADATA = {
    "id": 2917,
    "name": "Find the K-or of an Array",
    "slug": "find-the-k-or-of-an-array",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(1)",
    "description": "Find the bitwise OR of all elements in an array that have at least k set bits.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the bitwise OR of all elements in the array that have at least k set bits.

    Args:
        nums: A list of non-negative integers.
        k: The minimum number of set bits (1s) required for an element to be included.

    Returns:
        The bitwise OR of all elements in nums that have at least k set bits. 
        Returns 0 if no such elements exist.

    Examples:
        >>> solve([3, 1, 5], 2)
        3
        >>> solve([3, 1, 5], 3)
        0
        >>> solve([1, 2, 4, 8], 1)
        15
    """
    result_or = 0

    for num in nums:
        # Count the number of set bits (1s) in the current integer
        # bin(num).count('1') is efficient in Python for this purpose
        set_bits_count = bin(num).count('1')

        # If the count meets or exceeds the threshold k, include it in the OR result
        if set_bits_count >= k:
            result_or |= num

    return result_or
