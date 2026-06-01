METADATA = {
    "id": 2729,
    "name": "Check if The Number is Fascinating",
    "slug": "check-if-the-number-is-fascinating",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map", "bitmask"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Determine if a number is fascinating by checking if its digits and the digits 1-9 concatenated contain all digits from 1 to 9.",
}

def solve(num: int) -> bool:
    """
    Checks if the given number is 'fascinating'.
    
    A number is fascinating if, when concatenated with the digits 1 through 9,
    the resulting sequence contains all digits from 1 to 9 at least once.

    Args:
        num: The integer to check.

    Returns:
        True if the number is fascinating, False otherwise.

    Examples:
        >>> solve(192)
        True
        >>> solve(46)
        False
    """
    # We use a bitmask to track the presence of digits 1-9.
    # A bitmask is more space-efficient than a set or boolean array.
    # The target mask for digits 1-9 is (1 << 10) - 2, which is 1111111110 in binary.
    # However, it's simpler to check if the mask equals (1 << 10) - 2 or 
    # just check if bits 1 through 9 are set.
    seen_mask = 0
    
    # Process the digits of the input number
    temp_num = num
    while temp_num > 0:
        digit = temp_num % 10
        if digit != 0:
            seen_mask |= (1 << digit)
        temp_num //= 10
        
    # Process the digits 1 through 9
    for i in range(1, 10):
        seen_mask |= (1 << i)
        
    # The number is fascinating if all bits from 1 to 9 are set.
    # The mask for digits 1-9 is 0b1111111110 (which is 1022)
    target_mask = 0
    for i in range(1, 10):
        target_mask |= (1 << i)
        
    return (seen_mask & target_mask) == target_mask
