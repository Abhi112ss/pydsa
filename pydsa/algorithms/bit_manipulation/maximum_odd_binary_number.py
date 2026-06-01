METADATA = {
    "id": 2864,
    "name": "Maximum Odd Binary Number",
    "slug": "maximum-odd-binary-number",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum odd binary number by rearranging bits from a given binary string.",
}

def solve(binary: str) -> str:
    """
    Finds the maximum odd binary number that can be formed by rearranging the bits.
    
    To maximize the value, we want all '1's to be as far left as possible.
    To ensure the number is odd, the last bit must be '1'.
    
    Args:
        binary: A string representing a binary number.
        
    Returns:
        A string representing the maximum odd binary number.
        
    Examples:
        >>> solve("010")
        '10'
        >>> solve("1110")
        '111'
        >>> solve("0101")
        '1101'
    """
    # Count the number of ones and zeros in the input string
    ones_count = binary.count('1')
    zeros_count = binary.count('0')
    
    # To make the number odd, we must reserve one '1' for the last position.
    # The remaining (ones_count - 1) '1's should be placed at the most significant positions.
    # All '0's should be placed in the middle to keep the '1's at the front.
    
    # Construct the result:
    # 1. (ones_count - 1) ones
    # 2. All zeros
    # 3. The final one to ensure it is odd
    
    # We use string multiplication for efficient construction
    result = ('1' * (ones_count - 1)) + ('0' * zeros_count) + '1'
    
    return result
