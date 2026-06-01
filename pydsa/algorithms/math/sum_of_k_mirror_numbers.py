METADATA = {
    "id": 2081,
    "name": "Sum of k-Mirror Numbers",
    "slug": "sum-of-k-mirror-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "palindrome"],
    "difficulty": "hard",
    "time_complexity": "O(10^(k/2))",
    "space_complexity": "O(1)",
    "description": "Find the sum of the first k k-mirror numbers, which are palindromes with exactly k digits.",
}

def solve(k: int) -> int:
    """
    Calculates the sum of the first k k-mirror numbers.
    A k-mirror number is a palindrome with exactly k digits.

    Args:
        k (int): The number of digits in the palindromes to sum.

    Returns:
        int: The sum of the first k k-mirror numbers.

    Examples:
        >>> solve(1)
        45  # 1+2+3+4+5+6+7+8+9
        >>> solve(2)
        495 # 11+22+33+44+55+66+77+88+99
    """
    MOD = 10**9 + 7
    total_sum = 0
    count = 0

    # To generate k-digit palindromes, we only need to iterate through 
    # the first half of the digits.
    # For k=3, half is 2 digits (10-99). For k=4, half is 2 digits (10-99).
    # The length of the 'prefix' that determines the palindrome is ceil(k/2).
    half_len = (k + 1) // 2
    
    # The smallest prefix for a k-digit number is 10^(half_len - 1)
    # e.g., k=3, half_len=2, start=10. k=4, half_len=2, start=10.
    start_prefix = 10**(half_len - 1)
    # The largest prefix is 10^(half_len) - 1
    end_prefix = 10**half_len - 1

    for prefix in range(start_prefix, end_prefix + 1):
        s_prefix = str(prefix)
        
        # Construct the palindrome by mirroring the prefix.
        # If k is odd, we don't repeat the last character of the prefix.
        # If k is even, we reverse the whole prefix.
        if k % 2 == 0:
            palindrome_str = s_prefix + s_prefix[::-1]
        else:
            palindrome_str = s_prefix + s_prefix[:-1][::-1]
            
        total_sum = (total_sum + int(palindrome_str)) % MOD
        count += 1
        
        # Stop once we have found k such numbers
        if count == k:
            break
            
    return total_sum
