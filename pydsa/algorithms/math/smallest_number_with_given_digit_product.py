METADATA = {
    "id": 2847,
    "name": "Smallest Number With Given Digit Product",
    "slug": "smallest-number-with-given-digit-product",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest positive integer whose digits multiply to a given number n.",
}

def solve(n: int) -> int:
    """
    Finds the smallest positive integer whose digits multiply to the given number n.

    The strategy is to greedily extract the largest possible single-digit factors 
    (from 9 down to 2) to minimize the number of digits in the result. 
    To ensure the resulting number is the smallest, the digits are sorted 
    in non-decreasing order.

    Args:
        n: The target product of the digits.

    Returns:
        The smallest integer whose digits multiply to n. 
        Returns -1 if no such integer exists.

    Examples:
        >>> solve(1)
        1
        >>> solve(10)
        25
        >>> solve(13)
        -1
        >>> solve(100)
        455
    """
    # Edge case: if n is 1, the smallest number is 1.
    if n == 1:
        return 1

    digits = []
    
    # Greedily extract the largest single-digit factors from 9 down to 2.
    # This minimizes the total number of digits in the final number.
    for factor in range(9, 1, -1):
        while n % factor == 0:
            digits.append(factor)
            n //= factor
            
    # If n is not 1 after extracting all single-digit factors, 
    # it means n has a prime factor > 7.
    if n > 1:
        return -1
        
    # To get the smallest number, sort the digits in ascending order.
    # For example, if digits are [5, 2], 25 is smaller than 52.
    digits.sort()
    
    # Convert the list of digits into a single integer.
    result = 0
    for digit in digits:
        result = result * 10 + digit
        
    return result
