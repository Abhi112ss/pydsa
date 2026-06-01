METADATA = {
    "id": 1062,
    "name": "Longest Repeating Substring",
    "slug": "longest_repeating_substring",
    "category": "String",
    "aliases": [],
    "tags": ["binary_search", "rolling_hash", "suffix_array", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the longest substring that occurs at least twice in a given string.",
}

def solve(s: str) -> str:
    """
    Finds the longest substring that appears at least twice in the input string.

    Args:
        s: The input string to search within.

    Returns:
        The longest repeating substring. If multiple exist, any one is returned.
        If no repeating substring exists, returns an empty string.

    Examples:
        >>> solve("abcd")
        ''
        >>> solve("aaaaa")
        'aaaa'
        >>> solve("banana")
        'ana'
    """
    n = len(s)
    if n == 0:
        return ""

    # Convert string to integers to facilitate rolling hash calculations
    nums = [ord(c) - ord('a') for c in s]
    
    # Constants for Rabin-Karp rolling hash
    # Using a large prime and a base to minimize collisions
    MOD = (1 << 61) - 1  # Mersenne prime
    BASE = 31

    def check(length: int) -> str:
        """
        Checks if there is any repeating substring of a specific length.
        Uses Rabin-Karp rolling hash to achieve O(n) average time.

        Args:
            length: The length of the substring to check.

        Returns:
            The repeating substring if found, otherwise an empty string.
        """
        if length == 0:
            return ""

        # Precompute BASE^length % MOD for rolling hash removal
        base_pow = pow(BASE, length, MOD)
        
        current_hash = 0
        # Compute hash for the first window
        for i in range(length):
            current_hash = (current_hash * BASE + nums[i]) % MOD
        
        # Store seen hashes and their starting indices to handle collisions
        seen_hashes = {current_hash: [0]}
        
        for i in range(1, n - length + 1):
            # Rolling hash: remove leading digit, add trailing digit
            current_hash = (current_hash * BASE - nums[i - 1] * base_pow + nums[i + length - 1]) % MOD
            
            if current_hash in seen_hashes:
                # Potential collision or match: verify actual substring to be safe
                current_sub = s[i : i + length]
                for start_idx in seen_hashes[current_hash]:
                    if s[start_idx : start_idx + length] == current_sub:
                        return current_sub
                seen_hashes[current_hash].append(i)
            else:
                seen_hashes[current_hash] = [i]
        
        return ""

    # Binary search on the length of the substring
    low = 1
    high = n - 1
    result = ""

    while low <= high:
        mid = (low + high) // 2
        candidate = check(mid)
        if candidate:
            # If a repeating substring of length 'mid' exists, try longer
            result = candidate
            low = mid + 1
        else:
            # Otherwise, try shorter
            high = mid - 1

    return result
