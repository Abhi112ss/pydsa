METADATA = {
    "id": 137,
    "name": "Single Number II",
    "slug": "single-number-ii",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the element that appears exactly once in an array where every other element appears exactly three times.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the single number in an array where every other element appears three times.

    Uses bitwise logic with two state variables (ones and twos) to track the 
    count of bits at each position modulo 3.

    Args:
        nums: A list of integers.

    Returns:
        The integer that appears exactly once.

    Examples:
        >>> solve([2, 2, 3, 2])
        3
        >>> solve([0, 1, 0, 1, 0, 1, 99])
        99
    """
    # 'ones' tracks bits that have appeared 1 time (mod 3)
    # 'twos' tracks bits that have appeared 2 times (mod 3)
    ones = 0
    twos = 0

    for num in nums:
        # Update 'twos' with bits that are already in 'ones' and appear again in 'num'
        twos |= (ones & num)
        
        # Update 'ones' using XOR to toggle bits appearing for the 1st or 3rd time
        ones ^= num
        
        # If a bit is in both 'ones' and 'twos', it has appeared 3 times.
        # We create a mask to clear these bits from both 'ones' and 'twos'.
        three_times_mask = ~(ones & twos)
        
        ones &= three_times_mask
        twos &= three_times_mask

    return ones
