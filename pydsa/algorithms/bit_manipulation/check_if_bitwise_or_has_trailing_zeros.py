METADATA = {
    "id": 2980,
    "name": "Check if Bitwise OR Has Trailing Zeros",
    "slug": "check-if-bitwise-or-has-trailing-zeros",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if the bitwise OR of all elements in an array has a specific number of trailing zeros.",
}

def solve(nums: list[int], k: int) -> bool:
    """
    Checks if the bitwise OR of all elements in the array has exactly k trailing zeros.

    Args:
        nums: A list of integers.
        k: The required number of trailing zeros.

    Returns:
        True if the bitwise OR of all elements has exactly k trailing zeros, False otherwise.

    Examples:
        >>> solve([1, 2, 4], 0)
        False
        >>> solve([1, 2, 4], 1)
        False
        >>> solve([2, 4, 8], 1)
        False
        >>> solve([2, 6, 10], 1)
        True
    """
    if not nums:
        return False

    # Compute the bitwise OR of all elements in the array
    bitwise_or_sum = 0
    for num in nums:
        bitwise_or_sum |= num

    # If the OR sum is 0, it technically has an infinite number of trailing zeros 
    # in a mathematical sense, but for bitwise problems, we check if it's 0.
    if bitwise_or_sum == 0:
        return k == 0 # Or handle based on specific problem constraints if 0 is possible

    # Count trailing zeros using bit manipulation
    # (bitwise_or_sum & -bitwise_or_sum) isolates the lowest set bit
    # Example: 12 (1100) & -12 (0100) = 4 (0100)
    lowest_set_bit = bitwise_or_sum & -bitwise_or_sum
    
    # Convert the value of the lowest set bit to its power-of-two exponent
    # Example: 4 -> 2 (since 2^2 = 4)
    trailing_zeros_count = lowest_set_bit.bit_length() - 1

    return trailing_zeros_count == k
