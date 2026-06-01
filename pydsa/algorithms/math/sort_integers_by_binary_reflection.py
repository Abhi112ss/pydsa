METADATA = {
    "id": 3769,
    "name": "Sort Integers by Binary Reflection",
    "slug": "sort_integers_by_binary_reflection",
    "category": "Sorting",
    "aliases": [],
    "tags": ["bit_manipulation", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort a list of integers based on their binary reflected values.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Sorts a list of integers based on their binary reflection.
    
    The binary reflection of an integer is calculated by taking its binary 
    representation, reversing the bits, and converting it back to an integer.
    Note: The reflection is relative to the bit-length of the original number.

    Args:
        nums: A list of integers to be sorted.

    Returns:
        A new list of integers sorted by their binary reflection values.

    Examples:
        >>> solve([1, 2, 3])
        [1, 2, 3]
        # 1 (01) -> 1 (10) is not quite right, let's clarify:
        # 1 (bin 1) -> rev 1 -> 1
        # 2 (bin 10) -> rev 01 -> 1
        # 3 (bin 11) -> rev 11 -> 3
        # Sorting [1, 2, 3] by [1, 1, 3] -> [1, 2, 3] or [2, 1, 3]
    """

    def get_binary_reflection(n: int) -> int:
        """Calculates the bitwise reversal of n based on its bit length."""
        if n == 0:
            return 0
        
        # Determine the number of bits required to represent n
        bit_length = n.bit_length()
        reflection = 0
        
        # Iterate through the bits and build the reversed number
        for i in range(bit_length):
            # If the i-th bit from the right is set
            if (n >> i) & 1:
                # Set the corresponding bit from the left in the reflection
                reflection |= (1 << (bit_length - 1 - i))
        
        return reflection

    # Sort the list using the reflection as the primary key.
    # Python's sort is stable, so original relative order is kept for ties.
    return sorted(nums, key=get_binary_reflection)
