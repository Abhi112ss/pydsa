METADATA = {
    "id": 3271,
    "name": "Hash Divided String",
    "slug": "hash-divided-string",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["strings", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a string can be divided into two non-empty substrings such that their hash values are equal.",
}

def solve(s: str) -> bool:
    """
    Determines if the string 's' can be split into two non-empty substrings 
    with equal hash values. The hash value is the sum of (ord(char) - ord('a') + 1).

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        True if such a split exists, False otherwise.

    Examples:
        >>> solve("abc")
        False
        >>> solve("abcd")
        False
        >>> solve("aaba")
        True
    """
    n = len(s)
    if n < 2:
        return False

    # Precompute the total hash value of the entire string
    # Hash(substring) = sum(ord(c) - ord('a') + 1)
    total_hash = 0
    for char in s:
        total_hash += ord(char) - ord('a') + 1

    # We iterate through the string, maintaining a running sum (left_hash)
    # for the first substring. The second substring's hash is (total_hash - left_hash).
    left_hash = 0
    
    # We iterate up to n-1 because both substrings must be non-empty
    for i in range(n - 1):
        left_hash += ord(s[i]) - ord('a') + 1
        right_hash = total_hash - left_hash
        
        # If the running sum equals the remaining sum, we found a valid split
        if left_hash == right_hash:
            return True

    return False
