METADATA = {
    "id": 2937,
    "name": "Make Three Strings Equal",
    "slug": "make-three-strings-equal",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make three strings equal by calculating the length of their longest common prefix.",
}

def solve(s1: str, s2: str, s3: str) -> int:
    """
    Calculates the minimum number of operations to make three strings equal.
    
    The optimal strategy is to find the longest common prefix (LCP) shared 
    by all three strings. Any character after the LCP must be removed 
    from all strings to make them identical.

    Args:
        s1: The first input string.
        s2: The second input string.
        s3: The third input string.

    Returns:
        The total number of character removals required.

    Examples:
        >>> solve("abcde", "abcde", "abcde")
        0
        >>> solve("abcde", "abcfg", "abxyz")
        9
        >>> solve("a", "b", "c")
        3
    """
    # Determine the minimum length among the three strings to avoid index out of bounds
    min_length = min(len(s1), len(s2), len(s3))
    common_prefix_length = 0

    # Iterate through the strings up to the shortest length
    for i in range(min_length):
        # If all characters at the current index are identical, increment prefix length
        if s1[i] == s2[i] == s3[i]:
            common_prefix_length += 1
        else:
            # Stop as soon as a mismatch is found
            break

    # The number of operations is the sum of characters to be removed from each string
    # to reach the common prefix length.
    removals_s1 = len(s1) - common_prefix_length
    removals_s2 = len(s2) - common_prefix_length
    removals_s3 = len(s3) - common_prefix_length

    return removals_s1 + removals_s2 + removals_s3
