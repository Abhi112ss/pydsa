METADATA = {
    "id": 136,
    "name": "Single Number",
    "slug": "single-number",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "xor"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the element in an integer array that appears only once, while every other element appears twice.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the single number in a list where every other element appears twice.

    Args:
        nums: A list of integers where every element appears twice except for one.

    Returns:
        The integer that appears exactly once in the list.

    Examples:
        >>> solve([2, 2, 1])
        1
        >>> solve([4, 1, 2, 1, 2])
        4
        >>> solve([1])
        1
    """
    # Initialize the result with 0. 
    # XORing any number with 0 results in the number itself (x ^ 0 = x).
    result = 0
    
    for number in nums:
        # The XOR operation has three key properties used here:
        # 1. x ^ x = 0 (Any number XORed with itself is zero)
        # 2. x ^ 0 = x (Any number XORed with zero is itself)
        # 3. x ^ y = y ^ x (Commutative property)
        # By XORing all numbers, the pairs will cancel each other out to 0,
        # leaving only the unique number.
        result ^= number
        
    return result
