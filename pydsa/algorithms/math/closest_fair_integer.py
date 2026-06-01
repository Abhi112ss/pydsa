METADATA = {
    "id": 2417,
    "name": "Closest Fair Integer",
    "slug": "closest-fair-integer",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the closest integer to n that has an even sum of digits.",
}

def get_digit_sum(number: int) -> int:
    """Calculates the sum of the digits of a given integer.

    Args:
        number: The integer to process.

    Returns:
        The sum of the digits.
    """
    digit_sum = 0
    temp = abs(number)
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    return digit_sum

def solve(n: int) -> int:
    """Finds the closest integer to n that has an even sum of digits.

    If there is a tie (two integers are equally close), the smaller integer is returned.

    Args:
        n: The target integer.

    Returns:
        The closest integer with an even digit sum.

    Examples:
        >>> solve(3)
        2
        >>> solve(4)
        4
        >>> solve(15)
        15
    """
    # Check if n itself is fair (even digit sum)
    if get_digit_sum(n) % 2 == 0:
        return n

    # If n is not fair, the closest fair integer must be either n-1 or n+1.
    # This is because changing the last digit by 1 always flips the parity 
    # of the digit sum (unless we deal with carries, but even then, 
    # the parity of the sum of digits changes by 1 or an odd amount).
    
    # Check n-1 first to handle the tie-breaking rule (return smaller integer)
    lower_candidate = n - 1
    if get_digit_sum(lower_candidate) % 2 == 0:
        return lower_candidate

    # If n-1 wasn't fair, n+1 must be fair
    upper_candidate = n + 1
    if get_digit_sum(upper_candidate) % 2 == 0:
        return upper_candidate

    # This part is logically unreachable for n > 0 because parity flips every step
    return n
