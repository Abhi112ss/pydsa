METADATA = {
    "id": 866,
    "name": "Prime Palindrome",
    "slug": "prime-palindrome",
    "category": "Math",
    "aliases": [],
    "tags": ["prime_number", "palindrome", "enumeration"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(N))",
    "space_complexity": "O(1)",
    "description": "Find the smallest prime palindrome greater than or equal to n.",
}

def is_prime(num: int) -> bool:
    """Checks if a number is prime using trial division up to sqrt(num)."""
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check divisors using 6k +/- 1 rule
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(n: int) -> int:
    """
    Finds the smallest prime palindrome greater than or equal to n.
    
    The algorithm leverages the mathematical property that all even-length 
    palindromes are divisible by 11. Therefore, we only need to check 
    odd-length palindromes, except for the number 11 itself.

    Args:
        n: The starting integer.

    Returns:
        The smallest prime palindrome >= n.

    Examples:
        >>> solve(8)
        11
        >>> solve(11)
        11
        >>> solve(12)
        101
        >>> solve(1000)
        10301
    """
    if n <= 2:
        return 2
    
    # Special case: 11 is the only even-length prime palindrome
    if n <= 11 <= 101:
        # Check if n is within range where 11 is the next prime palindrome
        # However, if n is between 2 and 11, we must check if 2, 3, 5, 7 are >= n
        for p in [2, 3, 5, 7, 11]:
            if p >= n:
                return p

    # We generate palindromes by constructing the first half and mirroring it.
    # To find the smallest palindrome >= n, we iterate through possible lengths.
    # Even length palindromes (except 11) are divisible by 11, so we skip them.
    
    # Start by checking the current number if it's a palindrome and prime
    # But it's more efficient to generate palindromes by length.
    
    # We iterate through lengths of the 'half' of the palindrome.
    # For a palindrome of length L, the half has length (L+1)//2.
    # Example: Length 3 palindrome (101) -> half is 10.
    # Example: Length 5 palindrome (10001) -> half is 100.
    
    # We start from the length of n and go upwards.
    s_n = str(n)
    len_n = len(s_n)
    
    # We iterate through possible lengths of the palindrome
    for length in range(len_n, 10): # 10^8 is a safe upper bound for this problem
        # Skip even lengths unless length is 2 (which is handled by the 11 check)
        if length > 2 and length % 2 == 0:
            continue
            
        half_len = (length + 1) // 2
        start = 10**(half_len - 1)
        end = 10**half_len
        
        for half in range(start, end):
            # Construct the palindrome from the half
            s_half = str(half)
            if length % 2 == 0:
                # Even length: mirror the whole half (e.g., 12 -> 1221)
                # Note: We skip even lengths > 2, but included for completeness
                palindrome = int(s_half + s_half[::-1])
            else:
                # Odd length: mirror all but the last digit (e.g., 12 -> 121)
                palindrome = int(s_half + s_half[:-1][::-1])
            
            # If the generated palindrome is >= n and is prime, return it
            if palindrome >= n and is_prime(palindrome):
                return palindrome
                
    return -1 # Should not be reached given problem constraints