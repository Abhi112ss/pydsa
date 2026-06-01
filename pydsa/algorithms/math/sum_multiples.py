METADATA = {
    "id": 2652,
    "name": "Sum Multiples",
    "slug": "sum-multiples",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the sum of all integers in the range [1, n] that are divisible by 3 and 5.",
}

def solve(n: int) -> int:
    """
    Calculates the sum of all integers from 1 to n that are divisible by both 3 and 5.

    Args:
        n (int): The upper bound of the range [1, n].

    Returns:
        int: The sum of integers divisible by 3 and 5.

    Examples:
        >>> solve(7)
        0
        >>> solve(15)
        15
        >>> solve(30)
        45
    """
    total_sum = 0
    
    # Iterate through every integer from 1 up to and including n
    for current_number in range(1, n + 1):
        # A number is divisible by both 3 and 5 if it is divisible by 15
        # (since 3 and 5 are coprime, their least common multiple is 15)
        if current_number % 3 == 0 and current_number % 5 == 0:
            total_sum += current_number
            
    return total_sum
