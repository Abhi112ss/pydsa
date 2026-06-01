METADATA = {
    "id": 1044,
    "name": "Longest Duplicate Substring",
    "slug": "longest_duplicate_substring",
    "category": "String",
    "aliases": [],
    "tags": ["binary_search", "rolling_hash", "suffix_array"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the longest substring that occurs at least twice in a given string using binary search and Rabin-Karp rolling hash.",
}

def solve(s: str) -> str:
    """
    Finds the longest duplicate substring in a given string using binary search 
    on the length and Rabin-Karp rolling hash to detect duplicates.

    Args:
        s: The input string.

    Returns:
        The longest substring that appears at least twice. If no duplicate 
        exists, returns an empty string.

    Examples:
        >>> solve("banana")
        'ana'
        >>> solve("abcd")
        ''
    """
    n = len(s)
    # Convert characters to integers to facilitate rolling hash calculations
    nums = [ord(c) - ord('a') for c in s]
    
    # Large prime for modulo to minimize collisions
    # Using a large prime like 2**61 - 1 (Mersenne prime) is very effective
    MOD = (1 << 61) - 1
    BASE = 26

    def check(length: int) -> str | None:
        """
        Checks if there is a duplicate substring of a specific length.
        
        Args:
            length: The length of the substring to check.
            
        Returns:
            The duplicate substring if found, otherwise None.
        """
        if length == 0:
            return ""
        
        # Precompute BASE^length % MOD for rolling hash window sliding
        base_pow = pow(BASE, length, MOD)
        
        current_hash = 0
        for i in range(length):
            current_hash = (current_hash * BASE + nums[i]) % MOD
            
        # Store seen hashes in a set for O(1) average lookup
        seen = {current_hash}
        
        for i in range(1, n - length + 1):
            # Rolling hash: remove leading digit, add trailing digit
            # Formula: (Hash * BASE - leading_digit * BASE^length + new_digit) % MOD
            current_hash = (current_hash * BASE - nums[i - 1] * base_pow + nums[i + length - 1]) % MOD
            
            # Handle negative results from modulo in Python (though Python's % is usually safe)
            if current_hash < 0:
                current_hash += MOD
                
            if current_hash in seen:
                # In a production environment with high collision risk, 
                # one should verify the actual substring here.
                # For LeetCode constraints, a large prime is sufficient.
                return s[i : i + length]
            seen.add(current_hash)
            
        return None

    # Binary search for the maximum possible length of a duplicate substring
    low = 1
    high = n - 1
    result = ""
    
    while low <= high:
        mid = (low + high) // 2
        candidate = check(mid)
        
        if candidate is not None:
            # If a duplicate of length 'mid' exists, try longer lengths
            result = candidate
            low = mid + 1
        else:
            # If no duplicate of length 'mid' exists, try shorter lengths
            high = mid - 1
            
    return result
