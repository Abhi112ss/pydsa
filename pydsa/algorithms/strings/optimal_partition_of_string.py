METADATA = {
    "id": 2405,
    "name": "Optimal Partition of String",
    "slug": "optimal-partition-of-string",
    "category": "String",
    "aliases": [],
    "tags": ["hash_set", "strings", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Partition a string into the minimum number of substrings such that each substring contains only unique characters.",
}

def solve(s: str) -> int:
    """
    Partitions the string into the minimum number of substrings where each 
    substring contains only unique characters using a greedy approach.

    Args:
        s: The input string to be partitioned.

    Returns:
        The minimum number of substrings required.

    Examples:
        >>> solve("abacaba")
        4
        >>> solve("abaccc")
        3
    """
    if not s:
        return 0

    # We use a set to track characters in the current substring.
    # Since the alphabet size is constant (26 lowercase letters), 
    # the space complexity is O(1).
    seen_characters = set()
    partition_count = 1

    for char in s:
        # If the character is already in the current substring,
        # we must start a new partition.
        if char in seen_characters:
            partition_count += 1
            seen_characters.clear()
        
        # Add the current character to the current partition's set.
        seen_characters.add(char)

    return partition_count
