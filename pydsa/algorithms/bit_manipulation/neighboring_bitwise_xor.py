METADATA = {
    "id": 2683,
    "name": "Neighboring Bitwise XOR",
    "slug": "neighboring-bitwise-xor",
    "category": "Array",
    "aliases": [],
    "tags": ["bit_manipulation", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Construct an array of length n where each element at index i is the bitwise XOR of elements at indices i-1 and i+1 from the input array.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Constructs an array where each element is the bitwise XOR of its neighbors.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        A list of integers where result[i] = nums[i-1] ^ nums[i+1].
        For the first and last elements, the missing neighbor is treated as 0.

    Examples:
        >>> solve([1, 1, 0, 1, 0, 3, 3])
        [1, 1, 2, 0, 4, 3, 3]
        >>> solve([1, 1])
        [1, 1]
    """
    n = len(nums)
    result = [0] * n

    for i in range(n):
        # Determine the left neighbor: if i is 0, the neighbor is 0
        left_neighbor = nums[i - 1] if i > 0 else 0
        
        # Determine the right neighbor: if i is the last index, the neighbor is 0
        right_neighbor = nums[i + 1] if i < n - 1 else 0
        
        # Apply the bitwise XOR operation on the neighbors
        result[i] = left_neighbor ^ right_neighbor

    return result
