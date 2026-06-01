METADATA = {
    "id": 3158,
    "name": "Find the XOR of Numbers Which Appear Twice",
    "slug": "find-the-xor-of-numbers-which-appear-twice",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["bit_manipulation", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the XOR sum of all integers that appear exactly twice in a given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the XOR sum of all elements that appear exactly twice in the input list.

    Args:
        nums: A list of integers where some elements appear once and others appear twice.

    Returns:
        The result of XORing all numbers that appear exactly twice.

    Examples:
        >>> solve([1, 2, 1, 3, 2])
        3
        >>> solve([1, 1, 2, 2, 3, 3])
        0
    """
    counts: dict[int, int] = {}
    
    # Count the frequency of each number in the array
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    xor_sum = 0
    # Iterate through the frequency map and XOR numbers with a count of 2
    for num, count in counts.items():
        if count == 2:
            xor_sum ^= num
            
    return xor_sum
