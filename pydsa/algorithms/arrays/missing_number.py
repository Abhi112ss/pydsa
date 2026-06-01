METADATA = {
    "id": 268,
    "name": "Missing Number",
    "slug": "missing_number",
    "category": "array",
    "aliases": [],
    "tags": ["bit_manipulation", "math", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the missing number in the range [0, n] given an array of n distinct numbers.",
}


def solve(nums: list[int]) -> int:
    """Find the missing number in the range [0, n] using XOR.

    Args:
        nums: A list of distinct integers where each integer is in the range
              [0, n] and exactly one number is missing.

    Returns:
        The missing integer.

    Examples:
        >>> solve([3, 0, 1])
        2
        >>> solve([0])
        1
    """
    # Compute XOR of all numbers from 0 to n (inclusive)
    xor_all = 0
    for index in range(len(nums) + 1):
        xor_all ^= index

    # Compute XOR of all numbers present in the array
    xor_nums = 0
    for number in nums:
        xor_nums ^= number

    # The missing number is the XOR of the two results
    missing_number = xor_all ^ xor_nums
    return missing_number