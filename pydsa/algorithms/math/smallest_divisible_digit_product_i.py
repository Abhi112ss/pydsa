METADATA = {
    "id": 3345,
    "name": "Smallest Divisible Digit Product I",
    "slug": "smallest-divisible-digit-product-i",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest number whose digits multiply to a given target number.",
}

def solve(n: int) -> int:
    """
    Finds the smallest positive integer whose digits, when multiplied, equal n.

    The strategy is to greedily extract the largest possible single-digit 
    prime factors (9, 8, 7, 6, 5, 4, 3, 2) from the target number n. 
    By extracting larger digits first, we minimize the total number of digits, 
    and by sorting them at the end, we ensure the smallest numerical value.

    Args:
        n: The target product of digits.

    Returns:
        The smallest integer whose digits multiply to n. 
        Returns -1 if no such integer exists.

    Examples:
        >>> solve(12)
        26
        >>> solve(10)
        25
        >>> solve(13)
        -1
    """
    # Edge case: if n is 0, the smallest number is 0 (though problem context 
    # usually implies positive integers, we handle n < 10).
    if n < 10:
        return n

    digits = []
    temp_n = n

    # Greedy approach: Try to divide by the largest possible single digits first.
    # We start from 9 down to 2 to minimize the number of digits in the result.
    for divisor in range(9, 1, -1):
        while temp_n % divisor == 0:
            digits.append(divisor)
            temp_n //= divisor

    # If temp_n is not 1, it means n had a prime factor > 7 (like 11, 13, etc.)
    # which cannot be represented by a single digit.
    if temp_n > 1:
        return -1

    # To get the smallest number, sort the digits in non-decreasing order.
    # For example, if digits are [6, 2], 26 is smaller than 62.
    digits.sort()
    
    # Convert the list of digits into a single integer.
    result_str = "".join(map(str, digits))
    return int(result_str)
