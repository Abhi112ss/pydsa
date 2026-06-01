METADATA = {
    "id": 2981,
    "name": "Find Longest Special Substring That Occurs Thrice I",
    "slug": "find-longest-special-substring-that-occurs-thrice-i",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "suffix_array", "rolling_hash", "binary_search"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the longest substring that appears at least three times in a given string.",
}

def solve(s: str) -> str:
    """
    Finds the longest substring that occurs at least three times in the input string.

    Args:
        s: The input string to search within.

    Returns:
        The longest substring that appears at least three times. 
        If multiple exist with the same length, the one appearing earliest is returned.
        If no such substring exists, returns an empty string.

    Examples:
        >>> solve("aaaaa")
        "aaa"
        >>> solve("abacaba")
        "a"
        >>> solve("abcde")
        ""
    """
    n = len(s)
    if n < 3:
        return ""

    # Convert string to integers to facilitate rolling hash
    nums = [ord(c) - ord('a') + 1 for c in s]
    
    # Constants for rolling hash to minimize collisions
    # Using a large prime and a base
    MOD = (1 << 61) - 1  # Mersenne prime
    BASE = 31

    def get_repeated_substring(length: int) -> str:
        """
        Checks if there is a substring of a given length that occurs at least 3 times.
        Returns the substring if found, otherwise an empty string.
        """
        if length == 0:
            return ""
        
        # Precompute base^length % MOD
        power_len = pow(BASE, length, MOD)
        
        # Compute initial hash for the first window
        current_hash = 0
        for i in range(length):
            current_hash = (current_hash * BASE + nums[i]) % MOD
            
        # Dictionary to store frequency of hashes
        # Key: hash value, Value: list of starting indices to handle collisions
        hash_map: dict[int, list[int]] = {current_hash: [0]}
        
        for i in range(1, n - length + 1):
            # Rolling hash update: remove leading char, add trailing char
            current_hash = (current_hash * BASE - nums[i - 1] * power_len + nums[i + length - 1]) % MOD
            # Ensure positive hash
            if current_hash < 0:
                current_hash += MOD
            
            if current_hash in hash_map:
                # Check for actual string equality to handle potential collisions
                # In a production environment with a 61-bit prime, collisions are extremely rare
                # but we verify to ensure correctness.
                current_sub = s[i : i + length]
                count = 0
                # We only need to check if this specific substring has appeared 3 times.
                # However, to keep O(N) average, we check the hash map.
                # For the sake of this problem's constraints and the 61-bit prime, 
                # we can rely on the hash or do a limited check.
                
                # Optimization: Instead of full string comparison every time, 
                # we track counts of hashes.
                hash_map[current_hash].append(i)
            else:
                hash_map[current_hash] = [i]
        
        # Find if any hash appears at least 3 times
        # To be strictly correct against collisions, we must verify the substrings
        best_start = -1
        for h, indices in hash_map.items():
            if len(indices) >= 3:
                # Verify if they are actually the same substring
                # Group indices by their actual substring content
                sub_counts: dict[str, int] = {}
                for idx in indices:
                    sub = s[idx : idx + length]
                    sub_counts[sub] = sub_counts.get(sub, 0) + 1
                    if sub_counts[sub] >= 3:
                        # We want the one that appears earliest in the string
                        # But the problem asks for the longest, and we are inside a fixed length check.
                        # If multiple substrings of same length exist, we need the one with smallest index.
                        # However, the binary search will find the max length.
                        # We'll return the first one we find that satisfies the condition.
                        # To be safe, we find the minimum index among all valid substrings.
                        pass
                
                # Refined check:
                for sub, count in sub_counts.items():
                    if count >= 3:
                        # Find the first occurrence index of this substring
                        first_idx = s.find(sub)
                        if best_start == -1 or first_idx < best_start:
                            best_start = first_idx
                            
        return s[best_start : best_start + length] if best_start != -1 else ""

    # Binary search for the maximum length
    low = 1
    high = n - 2
    ans = ""
    
    while low <= high:
        mid = (low + high) // 2
        candidate = get_repeated_substring(mid)
        if candidate:
            ans = candidate
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
