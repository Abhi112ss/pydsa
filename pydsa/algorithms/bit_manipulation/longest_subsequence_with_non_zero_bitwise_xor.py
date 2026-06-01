METADATA = {
    "id": 3702,
    "name": "Longest Subsequence With Non-Zero Bitwise XOR",
    "slug": "longest_subsequence_with_non_zero_bitwise_xor",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subsequence whose bitwise XOR sum is non-zero.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subsequence with a non-zero bitwise XOR sum.

    The logic follows a greedy approach:
    1. If the XOR sum of all elements is non-zero, the longest subsequence is the entire array.
    2. If the XOR sum is zero, we must remove at least one element to change the XOR sum.
    3. Removing an element `x` from a zero-sum set results in a new XOR sum equal to `x`.
    4. Therefore, if there exists any non-zero element in the array, removing it results 
       in a non-zero XOR sum of length n-1.
    5. If all elements are zero, no non-zero XOR sum can ever be formed.

    Args:
        nums: A list of non-negative integers.

    Returns:
        The length of the longest subsequence with a non-zero XOR sum. 
        Returns 0 if no such subsequence exists.

    Examples:
        >>> solve([1, 2, 3])
        3
        >>> solve([1, 1, 2, 2])
        3
        >>> solve([0, 0, 0])
        0
    """
    total_xor_sum = 0
    has_non_zero = False
    n = len(nums)

    for num in nums:
        total_xor_sum ^= num
        if num > 0:
            has_non_zero = True

    # Case 1: The XOR sum of the whole array is already non-zero.
    if total_xor_sum != 0:
        return n

    # Case 2: Total XOR is zero. We need to remove an element to make it non-zero.
    # If we remove an element 'x', the new XOR sum is (0 ^ x) = x.
    # To get a non-zero sum, we must remove an element 'x' where x != 0.
    if has_non_zero:
        return n - 1

    # Case 3: All elements are zero, so no subsequence can have a non-zero XOR.
    return 0
