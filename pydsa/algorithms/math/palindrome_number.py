METADATA = {
    "id": 9,
    "name": "Palindrome Number",
    "slug": "palindrome-number",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(1)",
    "description": "Determine whether an integer is a palindrome.",
}

def solve(x: int) -> bool:
    """
    Determines if an integer is a palindrome without converting it to a string.

    Args:
        x: The integer to check.

    Returns:
        True if x is a palindrome, False otherwise.

    Examples:
        >>> solve(121)
        True
        >>> solve(-121)
        False
        >>> solve(10)
        False
    """
    # Negative numbers are not palindromes (e.g., -121 != 121-)
    # Also, if the last digit is 0, the first digit must be 0 (only 0 itself satisfies this)
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    # We reverse the second half of the number. 
    # When the original number becomes less than or equal to the reversed half,
    # we have reached the middle of the number.
    while x > reversed_half:
        last_digit = x % 10
        reversed_half = (reversed_half * 10) + last_digit
        x //= 10

    # For even length numbers, x should equal reversed_half (e.g., 1221 -> x=12, reversed=12)
    # For odd length numbers, we discard the middle digit by reversed_half // 10 
    # (e.g., 121 -> x=1, reversed=12. 1 == 12 // 10)
    return x == reversed_half or x == reversed_half // 10
