METADATA = {
    "id": 3663,
    "name": "Find The Least Frequent Digit",
    "slug": "find_the_least_frequent_digit",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the digit that appears the least number of times in a given integer.",
}

def solve(num: int) -> int:
    """
    Finds the digit that appears the least number of times in the given integer.
    If multiple digits have the same minimum frequency, the smallest digit is returned.
    If the number is 0, the digit 0 is returned.

    Args:
        num (int): The input integer.

    Returns:
        int: The least frequent digit.

    Examples:
        >>> solve(122333)
        1
        >>> solve(44556)
        6
        >>> solve(0)
        0
    """
    # Handle the edge case for zero
    if num == 0:
        return 0

    # Use absolute value to handle negative integers if they occur
    n = abs(num)
    
    # Frequency array for digits 0-9
    digit_counts = [0] * 10

    # Iterate through digits using modulo and division
    while n > 0:
        digit = n % 10
        digit_counts[digit] += 1
        n //= 10

    # Initialize tracking variables
    # We want the minimum frequency among digits that actually appeared
    min_frequency = float('inf')
    result_digit = -1

    # Iterate through the frequency array to find the least frequent digit
    # Iterating 0-9 ensures we pick the smallest digit in case of ties
    for digit in range(10):
        count = digit_counts[digit]
        
        # We only consider digits that appeared at least once
        if 0 < count < min_frequency:
            min_frequency = count
            result_digit = digit

    return result_digit
