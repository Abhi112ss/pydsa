METADATA = {
    "id": 1987,
    "name": "Number of Unique Good Subsequences",
    "slug": "number-of-unique-good-subsequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of unique non-empty subsequences that do not contain leading zeros.",
}

def solve(num: str) -> int:
    """
    Calculates the number of unique non-empty subsequences that do not start with '0'.

    The algorithm uses dynamic programming to track the number of unique subsequences 
    ending in each digit (0-9). To avoid leading zeros, we only initialize the 
    DP state for non-zero digits or handle the first occurrence of '0' carefully.
    Actually, a simpler way is to track subsequences ending in each digit and 
    ensure the very first digit of any subsequence is not '0'.

    Args:
        num: A string representing a large integer.

    Returns:
        The number of unique good subsequences modulo 10^9 + 7.

    Examples:
        >>> solve("101")
        4
        # Subsequences: "1", "10", "11", "101"
        >>> solve("11")
        2
        # Subsequences: "1", "11"
    """
    MOD = 1_000_000_007
    
    # ends_with[i] stores the number of unique subsequences ending with digit i.
    # We use a size of 10 to represent digits 0-9.
    ends_with = [0] * 10
    
    # To handle the "no leading zero" constraint, we can think of it this way:
    # A "good" subsequence is any subsequence that doesn't start with '0'.
    # However, the problem is easier if we track all unique subsequences 
    # and subtract those that start with '0', OR more simply:
    # Only allow a subsequence to start if the digit is not '0'.
    
    # Let's refine the DP:
    # ends_with[d] = (sum of all ends_with[0...9]) + 1 (if d > 0)
    # But we must be careful not to double count.
    
    # Correct DP approach:
    # Let dp[d] be the number of unique subsequences ending in digit d.
    # When we encounter digit 'd':
    # New dp[d] = (sum(dp[0...9]) + (1 if d > 0 else 0)) % MOD
    # This ensures that if d > 0, we can start a new subsequence consisting only of 'd'.
    # If d == 0, we can only append '0' to existing subsequences (which must have started with non-zero).
    
    for char in num:
        digit = int(char)
        
        # Calculate the total number of existing unique subsequences
        total_sum = sum(ends_with) % MOD
        
        if digit > 0:
            # If digit is 1-9, it can extend any existing subsequence 
            # OR start a new subsequence consisting only of itself.
            ends_with[digit] = (total_sum + 1) % MOD
        else:
            # If digit is 0, it can only extend existing subsequences.
            # It cannot start a new subsequence because that would be a leading zero.
            ends_with[digit] = total_sum % MOD
            
    return sum(ends_with) % MOD
