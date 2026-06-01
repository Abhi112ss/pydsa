METADATA = {
    "id": 2554,
    "name": "Maximum Number of Integers to Choose From a Range I",
    "slug": "maximum-number-of-integers-to-choose-from-a-range-i",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of integers in the range [left, right] that are divisible by num.",
}

def solve(left: int, right: int, num: int) -> int:
    """
    Calculates the maximum number of integers in the range [left, right] 
    that are divisible by num.

    Args:
        left (int): The lower bound of the range (inclusive).
        right (int): The upper bound of the range (inclusive).
        num (int): The divisor.

    Returns:
        int: The count of integers in [left, right] divisible by num.

    Examples:
        >>> solve(1, 10, 3)
        3
        >>> solve(1, 10, 11)
        0
        >>> solve(5, 5, 5)
        1
    """
    # The number of multiples of 'num' in the range [1, X] is floor(X / num).
    # To find the count in [left, right], we calculate the count up to 'right'
    # and subtract the count up to 'left - 1'.
    
    count_up_to_right = right // num
    count_up_to_left_minus_one = (left - 1) // num
    
    return count_up_to_right - count_up_to_left_minus_one
