METADATA = {
    "id": 3817,
    "name": "Good Indices in a Digit String",
    "slug": "good_indices_in_a_digit_string",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find all indices in a digit string where a specific pattern occurs within a sliding window.",
}

def solve(digit_string: str, pattern: str) -> list[int]:
    """
    Identifies all starting indices in digit_string where the pattern matches 
    the substring of length len(pattern) starting at that index.

    Args:
        digit_string: The input string of digits.
        pattern: The target pattern to search for.

    Returns:
        A list of integers representing the starting indices of the pattern.

    Examples:
        >>> solve("121212", "121")
        [0, 2]
        >>> solve("000", "00")
        [0, 1]
    """
    n = len(digit_string)
    m = len(pattern)
    
    if m > n or m == 0:
        return []

    # Precompute the hash of the pattern
    # Using a large prime and base for a rolling hash to avoid collisions
    # Since we only deal with digits 0-9, base 10 or 11 is sufficient
    base = 10
    mod = 10**9 + 7
    
    pattern_hash = 0
    current_window_hash = 0
    high_power = 1  # This will be base^(m-1) % mod
    
    for i in range(m):
        pattern_hash = (pattern_hash * base + int(pattern[i])) % mod
        current_window_hash = (current_window_hash * base + int(digit_string[i])) % mod
        if i < m - 1:
            high_power = (high_power * base) % mod

    result = []
    
    # Check the first window
    if current_window_hash == pattern_hash:
        # Double check with actual string comparison to handle potential collisions
        if digit_string[0:m] == pattern:
            result.append(0)

    # Slide the window across the digit_string
    for i in range(1, n - m + 1):
        # Remove the leading digit
        leading_digit = int(digit_string[i - 1])
        current_window_hash = (current_window_hash - leading_digit * high_power) % mod
        
        # Add the trailing digit
        trailing_digit = int(digit_string[i + m - 1])
        current_window_hash = (current_window_hash * base + trailing_digit) % mod
        
        # Ensure hash is positive
        if current_window_hash < 0:
            current_window_hash += mod
            
        # If hashes match, verify the substring to ensure correctness
        if current_window_hash == pattern_hash:
            if digit_string[i : i + m] == pattern:
                result.append(i)
                
    return result
