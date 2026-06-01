METADATA = {
    "id": 2505,
    "name": "Bitwise OR of All Subsequence Sums",
    "slug": "bitwise-or-of-all-subsequence-sums",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the bitwise OR of all possible subsequence sums of a given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the bitwise OR of all possible subsequence sums of the input array.

    The key mathematical insight is that the bitwise OR of all subsequence sums 
    is equivalent to the bitwise OR of the individual elements themselves. 
    This is because any bit set in an element will contribute to at least 
    one subsequence sum (the element itself), and any bit set in a sum 
    must have been contributed by at least one element in that subsequence.

    Args:
        nums: A list of integers.

    Returns:
        The bitwise OR of all subsequence sums.

    Examples:
        >>> solve([1, 3])
        3
        >>> solve([1, 2, 3])
        3
        >>> solve([10, 5, 2])
        15
    """
    result_or = 0
    
    # Iterate through each number in the array
    for number in nums:
        # Perform bitwise OR with the current running result.
        # Since any bit present in an element will be present in the 
        # final OR of all sums, we simply OR all elements together.
        result_or |= number
        
    return result_or
