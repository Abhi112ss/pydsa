METADATA = {
    "id": 3303,
    "name": "Find the Occurrence of First Almost Equal Substring",
    "slug": "find-the-occurrence-of-first-almost-equal-substring",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "rolling_hash", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the first occurrence of a substring of length 'k' in 's' that differs from 'pattern' by at most one character.",
}

def solve(s: str, pattern: str, k: int) -> int:
    """
    Finds the first index in 's' where a substring of length 'k' is 'almost equal' 
    to 'pattern' (at most one character difference).

    Args:
        s: The source string to search within.
        pattern: The target pattern string.
        k: The length of the substring to compare.

    Returns:
        The starting index of the first almost equal substring, or -1 if none exists.

    Examples:
        >>> solve("abcde", "axc", 3)
        0
        >>> solve("abcdef", "xyz", 3)
        -1
    """
    n = len(s)
    m = len(pattern)
    
    # If the pattern is longer than the window k, we can't match it.
    # However, based on problem constraints, k is usually the length of pattern.
    # If k < m, we only compare the first k characters.
    # If k > m, the problem definition usually implies k == len(pattern).
    # We will assume we compare pattern[:k] with s[i:i+k].
    
    # Using Rolling Hash to find mismatches efficiently.
    # To find if there is at most 1 mismatch, we can use binary search + hashing
    # to find the first mismatch, then check if the remaining suffixes match.
    # However, for a fixed length k, we can use a sliding window approach.
    
    # Precompute hashes for s and pattern
    P = 31
    MOD = 10**9 + 9
    
    pow_p = [1] * (max(n, m) + 1)
    for i in range(1, len(pow_p)):
        pow_p[i] = (pow_p[i-1] * P) % MOD
        
    def compute_hashes(text: str) -> list[int]:
        h = [0] * (len(text) + 1)
        for i in range(len(text)):
            h[i+1] = (h[i] * P + ord(text[i])) % MOD
        return h

    hash_s = compute_hashes(s)
    hash_p = compute_hashes(pattern)

    def get_hash(h: list[int], left: int, right: int) -> int:
        """Returns hash of substring from index left to right (inclusive)."""
        res = (h[right + 1] - h[left] * pow_p[right - left + 1]) % MOD
        return (res + MOD) % MOD

    # We need to check every window of size k in s
    # Since we need to find the FIRST occurrence, we iterate i from 0 to n-k
    for i in range(n - k + 1):
        # Compare s[i : i+k] with pattern[0 : k]
        # We use binary search to find the first position where they differ
        
        low = 0
        high = k - 1
        first_mismatch = -1
        
        # Binary search for the first mismatch index within the window
        while low <= high:
            mid = (low + high) // 2
            # Check if prefix of length mid+1 matches
            if get_hash(hash_s, i, i + mid) == get_hash(hash_p, 0, mid):
                low = mid + 1
            else:
                first_mismatch = mid
                high = mid - 1
        
        if first_mismatch == -1:
            # Perfect match
            return i
        else:
            # One mismatch found at 'first_mismatch'. 
            # Check if the rest of the substring (after the mismatch) matches perfectly.
            # The rest starts at first_mismatch + 1 and ends at k - 1.
            if first_mismatch == k - 1:
                # Mismatch was at the very last character
                return i
            
            # Check suffix after the mismatch
            suffix_len = k - 1 - first_mismatch
            start_s = i + first_mismatch + 1
            start_p = first_mismatch + 1
            
            if get_hash(hash_s, start_s, start_s + suffix_len - 1) == \
               get_hash(hash_p, start_p, start_p + suffix_len - 1):
                return i
                
    return -1
