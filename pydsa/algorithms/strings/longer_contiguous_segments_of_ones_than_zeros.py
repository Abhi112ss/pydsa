METADATA = {
    "id": 1869,
    "name": "Longer Contiguous Segments of Ones than Zeros",
    "slug": "longer-contiguous-segments-of-ones-than-zeros",
    "category": "String",
    "aliases": [],
    "tags": ["string", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if the longest contiguous segment of ones is strictly longer than the longest contiguous segment of zeros in a binary string.",
}

def solve(s: str) -> bool:
    """
    Determines if the longest contiguous segment of '1's is strictly longer 
    than the longest contiguous segment of '0's.

    Args:
        s: A binary string consisting of '0's and '1's.

    Returns:
        True if the maximum length of consecutive '1's is greater than 
        the maximum length of consecutive '0's, False otherwise.

    Examples:
        >>> solve("1110011")
        True
        >>> solve("11100011")
        False
        >>> solve("10101")
        False
    """
    max_ones: int = 0
    max_zeros: int = 0
    
    current_ones: int = 0
    current_zeros: int = 0

    for char in s:
        if char == '1':
            # Increment current ones count and reset zeros count
            current_ones += 1
            current_zeros = 0
            # Update global maximum for ones
            if current_ones > max_ones:
                max_ones = current_ones
        else:
            # Increment current zeros count and reset ones count
            current_zeros += 1
            current_ones = 0
            # Update global maximum for zeros
            if current_zeros > max_zeros:
                max_zeros = current_zeros

    # The problem asks if the longest segment of ones is strictly longer
    return max_ones > max_zeros
