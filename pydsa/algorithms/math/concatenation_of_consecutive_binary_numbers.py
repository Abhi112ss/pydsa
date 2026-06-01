METADATA = {
    "id": 1680,
    "name": "Concatenation of Consecutive Binary Numbers",
    "slug": "concatenation-of-consecutive-binary-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest positive integer whose binary representation, when concatenated, contains the pattern '111'.",
}

def solve(pattern: str) -> int:
    """
    Finds the smallest positive integer such that the concatenation of its 
    binary representations (1, 2, ..., n) contains the given pattern.

    Args:
        pattern: A string representing the binary pattern to search for.

    Returns:
        The smallest integer n such that the concatenated binary string 
        contains the pattern.

    Examples:
        >>> solve("111")
        7
        >>> solve("01")
        1
        >>> solve("101")
        5
    """
    # We build the concatenated binary string incrementally.
    # Since the pattern length is small (up to 20), the integer n 
    # will not grow excessively large, allowing for a linear search.
    concatenated_binary = ""
    current_number = 1
    
    while True:
        # Convert current number to binary string without the '0b' prefix
        binary_representation = bin(current_number)[2:]
        concatenated_binary += binary_representation
        
        # Check if the pattern exists in the current concatenated string.
        # We only need to check the end of the string to optimize, 
        # but a simple 'in' check is efficient enough for these constraints.
        if pattern in concatenated_binary:
            return current_number
        
        current_number += 1
