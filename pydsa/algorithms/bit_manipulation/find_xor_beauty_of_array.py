METADATA = {
    "id": 2527,
    "name": "Find Xor-Beauty of Array",
    "slug": "find-xor-beauty-of-array",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the XOR sum of the XOR sums of all subarrays.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the XOR sum of the XOR sums of all possible subarrays.

    The XOR sum of all subarrays can be determined by calculating how many 
    subarrays each element `nums[i]` belongs to. An element at index `i` 
    is part of `(i + 1) * (n - i)` subarrays. If this count is odd, 
    `nums[i]` contributes to the final XOR sum; otherwise, it cancels out.

    Args:
        nums: A list of integers.

    Returns:
        The XOR sum of the XOR sums of all subarrays.

    Examples:
        >>> solve([1, 2, 3])
        2
        >>> solve([1, 1, 1])
        1
    """
    n = len(nums)
    xor_beauty = 0

    for i in range(n):
        # Calculate the number of subarrays that contain the element at index i.
        # A subarray is defined by its start index (0 to i) and end index (i to n-1).
        # Number of choices for start: (i + 1)
        # Number of choices for end: (n - i)
        count = (i + 1) * (n - i)

        # If the count is odd, the element contributes to the final XOR sum.
        # If the count is even, the element's XOR contribution is 0 (x ^ x = 0).
        if count % 2 == 1:
            xor_beauty ^= nums[i]

    return xor_beauty
