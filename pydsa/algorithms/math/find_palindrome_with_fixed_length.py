METADATA = {
    "id": 2217,
    "name": "Find Palindrome With Fixed Length",
    "slug": "find-palindrome-with-fixed-length",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the k-th palindrome of a fixed length n, or return -1 if it doesn't exist.",
}

def solve(int_n: int, int_k: int) -> int:
    """
    Finds the k-th palindrome of length n.

    A palindrome is determined by its first half. For a length n, the first 
    half has length ceil(n / 2). We can treat this half as a number that 
    starts from the smallest possible value for that length and increments.

    Args:
        int_n: The fixed length of the palindrome.
        int_k: The k-th palindrome to find (1-indexed).

    Returns:
        The k-th palindrome as an integer, or -1 if it does not exist.

    Examples:
        >>> solve(3, 1)
        101
        >>> solve(3, 2)
        111
        >>> solve(3, 9)
        999
        >>> solve(3, 10)
        -1
        >>> solve(4, 1)
        1001
    """
    # The number of digits that define the palindrome (the first half)
    # For n=3, half_len=2 (10, 11...); For n=4, half_len=2 (10, 11...)
    half_len = (int_n + 1) // 2
    
    # The smallest number with 'half_len' digits (e.g., if half_len=2, start=10)
    start_num = 10**(half_len - 1)
    
    # The largest number with 'half_len' digits (e.g., if half_len=2, end=99)
    # We use this to check if k-th palindrome exists
    max_num = 10**half_len - 1
    
    # Calculate the actual prefix for the k-th palindrome
    # Since k is 1-indexed, the k-th number is start_num + (k - 1)
    target_prefix = start_num + (int_k - 1)
    
    # If the target prefix exceeds the number of digits allowed, k is too large
    if target_prefix > max_num:
        return -1
    
    prefix_str = str(target_prefix)
    
    # Construct the full palindrome string
    # If n is odd, we don't repeat the last character of the prefix
    if int_n % 2 == 1:
        # For n=3, prefix="10", suffix="1" (reverse of "1")
        palindrome_str = prefix_str + prefix_str[:-1][::-1]
    else:
        # For n=4, prefix="10", suffix="01" (reverse of "10")
        palindrome_str = prefix_str + prefix_str[::-1]
        
    return int(palindrome_str)
