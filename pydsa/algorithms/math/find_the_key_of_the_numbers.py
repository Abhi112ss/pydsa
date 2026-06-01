METADATA = {
    "id": 3270,
    "name": "Find the Key of the Numbers",
    "slug": "find-the-key-of-the-numbers",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the key of a list of numbers by sorting them and applying bitwise OR iteratively.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the key of the numbers by sorting them and applying bitwise OR.

    The key is defined as the result of bitwise ORing all elements of the 
    sorted version of the input array.

    Args:
        nums: A list of integers.

    Returns:
        The integer result of the bitwise OR operation on the sorted list.

    Examples:
        >>> solve([1, 2, 3])
        3
        >>> solve([10, 5, 2])
        15
    """
    if not nums:
        return 0

    # Sort the numbers in non-decreasing order as per problem requirements
    nums.sort()

    # Initialize the key with the first element of the sorted list
    key = nums[0]

    # Iteratively apply the bitwise OR operation across all elements
    for i in range(1, len(nums)):
        key |= nums[i]

    return key
