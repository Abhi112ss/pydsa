METADATA = {
    "id": 1342,
    "name": "Number of Steps to Reduce a Number to Zero",
    "slug": "number-of-steps-to-reduce-a-number-to-zero",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of steps to reduce a number to zero by dividing by 2 if even and subtracting 1 if odd.",
}

def solve(num: int) -> int:
    """
    Calculates the number of steps to reduce a non-negative integer to zero.
    
    The rules are:
    - If the current number is even, divide it by 2.
    - If the current number is odd, subtract 1 from it.

    Args:
        num: A non-negative integer.

    Returns:
        The total number of steps taken to reach zero.

    Examples:
        >>> solve(14)
        6
        >>> solve(8)
        5
    """
    if num == 0:
        return 0

    # The problem can be viewed through bit manipulation:
    # 1. Every '1' bit requires two steps: one to subtract 1 (making it 0) 
    #    and one to divide by 2 (shifting it right).
    # 2. Every '0' bit (except the leading bit) requires one step: 
    #    just dividing by 2 (shifting it right).
    # 3. The very last '1' bit only requires one step (subtracting 1 to reach 0).
    
    # Total steps = (Total bits - 1) + (Number of set bits)
    # Example 14 (1110 in binary):
    # Bits: 4, Set bits: 3. Steps = (4-1) + 3 = 6.
    
    # Calculate the position of the highest set bit (total bits)
    bit_length = num.bit_length()
    
    # Count the number of set bits (1s)
    set_bits_count = bin(num).count('1')
    
    # The formula derived from the bit logic:
    # Each bit position (except the most significant) represents a division step.
    # Each '1' bit also represents a subtraction step.
    return (bit_length - 1) + set_bits_count
