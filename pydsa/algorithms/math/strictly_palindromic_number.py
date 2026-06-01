METADATA = {
    "id": 2396,
    "name": "Strictly Palindromic Number",
    "slug": "strictly-palindromic-number",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a number n is strictly palindromic in all bases from 2 to n-2.",
}

def solve(n: int) -> bool:
    """
    Determines if a number n is strictly palindromic.
    
    A number is strictly palindromic if it is a palindrome in every base 
    from 2 to n-2 inclusive. However, for any n > 4, the number n 
    represented in base n-2 is always '12' (since n = 1*(n-2) + 2), 
    which is not a palindrome. Therefore, the answer is always False 
    for n > 4.

    Args:
        n: The integer to check.

    Returns:
        True if the number is strictly palindromic, False otherwise.

    Examples:
        >>> solve(4)
        False
        >>> solve(5)
        False
    """
    # The problem asks to check bases from 2 to n-2.
    # If n <= 4, the range [2, n-2] is empty or invalid for the definition.
    # For any n > 4, consider base b = n - 2.
    # To represent n in base (n-2):
    # n = 1 * (n-2) + 2
    # The digits in base (n-2) are [1, 2].
    # [1, 2] is never a palindrome.
    # Thus, for all n > 4, the condition is impossible to satisfy.
    
    # Based on the constraints and the mathematical proof, 
    # the result is always False for the given problem constraints (n >= 4).
    return False
