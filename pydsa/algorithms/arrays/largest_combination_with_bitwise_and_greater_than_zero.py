METADATA = {
    "id": 2275,
    "name": "Largest Combination With Bitwise AND Greater Than Zero",
    "slug": "largest-combination-with-bitwise-and-greater-than-zero",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n * 32)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of elements in a subset such that their bitwise AND is greater than zero.",
}

def solve(candidates: list[int]) -> int:
    """
    Finds the maximum size of a subset of candidates whose bitwise AND is non-zero.

    The core idea is that for a bitwise AND of a subset to be greater than zero, 
    there must be at least one bit position that is set (1) in all elements of 
    that subset. Therefore, the problem reduces to finding the bit position 
    that is shared by the maximum number of elements.

    Args:
        candidates: A list of positive integers.

    Returns:
        The maximum number of elements that can form a subset with a bitwise AND > 0.

    Examples:
        >>> solve([16, 17, 15, 13, 2, 6, 8, 4])
        4
        >>> solve([1, 2, 3])
        2
    """
    max_subset_size = 0
    
    # Since the problem constraints usually imply 32-bit integers (or up to 10^9),
    # we iterate through each bit position from 0 to 31.
    for bit_position in range(32):
        current_bit_count = 0
        mask = 1 << bit_position
        
        for num in candidates:
            # Check if the bit at the current position is set
            if num & mask:
                current_bit_count += 1
        
        # The maximum count across all bit positions is our answer
        if current_bit_count > max_subset_size:
            max_subset_size = current_bit_count
            
    return max_subset_size
