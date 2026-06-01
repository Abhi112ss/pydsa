METADATA = {
    "id": 1461,
    "name": "Check If a String Contains All Binary Codes of Size K",
    "slug": "check-if-a-string-contains-all-binary-codes-of-size-k",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_set", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(2^k)",
    "description": "Determine if a binary string contains all possible $2^k$ binary codes of length $k$.",
}

def solve(s: str, k: int) -> bool:
    """
    Checks if the binary string 's' contains all possible binary codes of length 'k'.

    Args:
        s: A string consisting of '0's and '1's.
        k: The length of the binary codes to check for.

    Returns:
        True if all $2^k$ binary codes are present in 's', False otherwise.

    Examples:
        >>> solve("00110", 2)
        True
        >>> solve("010", 2)
        False
    """
    # Total number of unique binary codes of length k is 2^k
    total_required = 1 << k
    
    # Use a set to store unique substrings of length k found in s
    seen_codes = set()
    
    # The number of possible substrings of length k is len(s) - k + 1
    # We iterate through the string using a sliding window approach
    for i in range(len(s) - k + 1):
        # Extract the substring of length k
        substring = s[i : i + k]
        seen_codes.add(substring)
        
        # Optimization: If we've already found all possible codes, return True early
        if len(seen_codes) == total_required:
            return True
            
    return len(seen_codes) == total_required
