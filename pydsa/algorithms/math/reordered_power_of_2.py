METADATA = {
    "id": 869,
    "name": "Reordered Power of 2",
    "slug": "reordered-power-of-2",
    "category": "Math",
    "aliases": [],
    "tags": ["counting", "sorting", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log^2 n)",
    "space_complexity": "O(log n)",
    "description": "Determine if any permutation of the digits of a given integer n forms a power of 2.",
}

def solve(n: int) -> bool:
    """
    Determines if any permutation of the digits of n results in a power of 2.

    Args:
        n: The input integer.

    Returns:
        True if a permutation of n is a power of 2, False otherwise.

    Examples:
        >>> solve(1)
        True
        >>> solve(10)
        False
        >>> solve(46)
        True
    """
    # Helper to get a frequency count of digits in a number
    # We use a sorted tuple of digits as a canonical representation (hashable)
    def get_digit_signature(num: int) -> tuple[int, ...]:
        return tuple(sorted(int(digit) for digit in str(num)))

    # The target signature is the sorted digits of the input number
    target_signature = get_digit_signature(n)

    # Since n <= 10^9, we only need to check powers of 2 up to 2^30
    # (2^30 is approx 1.07 * 10^9)
    for exponent in range(31):
        power_of_two = 1 << exponent
        
        # If the digit counts match, then one is a permutation of the other
        if get_digit_signature(power_of_two) == target_signature:
            return True

    return False
