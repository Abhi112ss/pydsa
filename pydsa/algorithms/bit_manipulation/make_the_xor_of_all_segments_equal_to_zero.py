METADATA = {
    "id": 1787,
    "name": "Make the XOR of All Segments Equal to Zero",
    "slug": "make-the-xor-of-all-segments-equal-to-zero",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make the XOR sum of all segments equal to zero.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers representing the segments.

    Returns:
        The minimum number of operations required to make the XOR sum of all segments zero.
    """
    total_xor_sum = 0
    for num in nums:
        total_xor_sum ^= num

    if total_xor_sum == 0:
        return 0

    n = len(nums)
    prefix_xor = 0
    for i in range(n - 1):
        prefix_xor ^= nums[i]
        if prefix_xor == 0:
            return 1

    return 2