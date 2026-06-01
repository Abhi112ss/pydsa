METADATA = {
    "id": 1316,
    "name": "Distinct Echo Substrings",
    "slug": "distinct-echo-substrings",
    "category": "String",
    "aliases": [],
    "tags": ["string_hashing", "rolling_hash", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the number of distinct non-empty substrings of s that can be written as the concatenation of some string with itself.",
}

def solve(s: str) -> int:
    """
    Finds the number of distinct substrings that are formed by repeating a string twice.

    Args:
        s: The input string.

    Returns:
        The count of distinct echo substrings.

    Examples:
        >>> solve("abcabcabc")
        2
        >>> solve("leetcodeleetcode")
        2
    """
    n = len(s)
    if n < 2:
        return 0

    # Using two large primes and a base for double hashing to minimize collisions.
    # However, for O(n^2) in Python, a single large prime with a large base 
    # is often sufficient and faster due to constant factors.
    MOD = (1 << 61) - 1  # Mersenne prime
    BASE = 31
    
    # Precompute prefix hashes and powers of BASE
    # hash_values[i] stores the hash of s[0...i-1]
    hash_values = [0] * (n + 1)
    powers = [1] * (n + 1)
    
    for i in range(n):
        hash_values[i + 1] = (hash_values[i] * BASE + (ord(s[i]) - ord('a') + 1)) % MOD
        powers[i + 1] = (powers[i] * BASE) % MOD

    def get_hash(left: int, right: int) -> int:
        """Returns the hash of the substring s[left:right]."""
        res = (hash_values[right] - hash_values[left] * powers[right - left]) % MOD
        return res

    distinct_echoes = set()

    # Iterate through all possible lengths of the repeating part 't'
    # The total length of the echo substring is 2 * length
    for length in range(1, n // 2 + 1):
        # Use a sliding window of size 2 * length
        for i in range(n - 2 * length + 1):
            # Substring 1: s[i : i + length]
            # Substring 2: s[i + length : i + 2 * length]
            
            # Compare hashes of the two adjacent halves
            hash1 = get_hash(i, i + length)
            hash2 = get_hash(i + length, i + 2 * length)
            
            if hash1 == hash2:
                # If hashes match, add the hash of the whole echo substring to the set
                # to ensure we only count distinct substrings.
                distinct_echoes.add(hash1)

    return len(distinct_echoes)
