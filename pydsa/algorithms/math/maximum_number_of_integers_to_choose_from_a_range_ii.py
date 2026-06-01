METADATA = {
    "id": 2557,
    "name": "Maximum Number of Integers to Choose From a Range II",
    "slug": "maximum-number-of-integers-to-choose-from-a-range-ii",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of integers in a range [left, right] that are divisible by a given num.",
}

def solve(left: int, right: int, num: int) -> int:
    """
    Calculates the maximum number of integers in the range [left, right] 
    that are divisible by 'num'.

    Args:
        left (int): The start of the range (inclusive).
        right (int): The end of the range (inclusive).
        num (int): The divisor.

    Returns:
        int: The count of integers in [left, right] divisible by num.

    Examples:
        >>> solve(1, 10, 2)
        5
        >>> solve(1, 10, 11)
        0
        >>> solve(10, 20, 5)
        3
    """
    # The number of multiples of 'num' in the range [1, X] is floor(X / num).
    # To find the count in [left, right], we calculate:
    # count(1 to right) - count(1 to left - 1)
    
    # Count multiples from 1 up to 'right'
    count_up_to_right = right // num
    
    # Count multiples from 1 up to 'left - 1'
    count_up_to_left_minus_one = (left - 1) // num
    
    # The difference gives the count within the inclusive range [left, right]
    return count_up_to_right - count_up_to_left_minus_one
