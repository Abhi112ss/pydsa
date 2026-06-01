METADATA = {
    "id": 479,
    "name": "Largest Palindrome Product",
    "slug": "largest-palindrome-product",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "palindrome"],
    "difficulty": "hard",
    "time_complexity": "O(10^n)",
    "space_complexity": "O(1)",
    "description": "Find the largest palindrome made from the product of two n-digit numbers.",
}

def solve(n: int) -> int:
    """
    Finds the largest palindrome made from the product of two n-digit numbers.

    Args:
        n: The number of digits for each factor.

    Returns:
        The largest palindrome product.

    Examples:
        >>> solve(1)
        9
        >>> solve(2)
        9009
        >>> solve(3)
        906609
    """
    if n == 1:
        return 9

    # The largest n-digit number (e.g., 99 for n=2)
    upper_limit = 10**n - 1
    # The smallest n-digit number (e.g., 10 for n=2)
    lower_limit = 10**(n - 1)

    # We iterate downwards from the largest possible palindrome.
    # A palindrome of length 2n can be represented as:
    # upper_half * 10^n + reverse(upper_half)
    # Example for n=2: upper_half = 99 -> 99 * 100 + 99 = 9999
    # However, the standard construction is: upper_half * 10^(n-1) + reverse(upper_half)
    # Wait, for n=2, max palindrome is 9009. 
    # Let's use the construction: upper_half * 10^n + reverse(upper_half) is wrong.
    # Correct construction for 2n-digit palindrome:
    # Let upper_half be the first n digits.
    # Palindrome = upper_half * 10^n + reverse(upper_half) is for 2n digits? 
    # No, if n=2, upper_half is 99. 99 * 10^2 + 99 = 9999. Correct.
    # But 9009 is the largest for n=2. 9009 comes from upper_half = 90.
    # 90 * 10^2 + 09 = 9009.
    
    # Iterate through possible upper halves of the palindrome in descending order
    for upper_half in range(upper_limit, lower_limit - 1, -1):
        # Construct the palindrome from the upper half
        s_half = str(upper_half)
        palindrome = int(s_half + s_half[::-1])
        
        # Check if this palindrome can be factored into two n-digit numbers
        # We only need to check factors from upper_limit down to sqrt(palindrome)
        # because if palindrome = a * b and a > b, then a must be >= sqrt(palindrome)
        # and since we want the largest palindrome, we check factors starting from upper_limit.
        for factor_a in range(upper_limit, lower_limit - 1, -1):
            # Optimization: if factor_a squared is less than the palindrome, 
            # no need to check further for this palindrome as factor_b would be > factor_a
            if factor_a * factor_a < palindrome:
                break
                
            if palindrome % factor_a == 0:
                factor_b = palindrome // factor_a
                # Check if the second factor is also within the n-digit range
                if lower_limit <= factor_b <= upper_limit:
                    return palindrome

    return -1  # Should not be reached for n >= 1