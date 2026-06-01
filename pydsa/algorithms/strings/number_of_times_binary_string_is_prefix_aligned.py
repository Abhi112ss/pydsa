METADATA = {
    "id": 1375,
    "name": "Number of Times Binary String Is Prefix-Aligned",
    "slug": "number-of-times-binary-string-is-prefix-aligned",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count how many times the prefix of a binary string matches the pattern of the target string.",
}

def solve(pattern: str, binary: str) -> int:
    """
    Counts the number of times the prefix of the 'binary' string matches 
    the 'pattern' string.

    A prefix of length 'i' matches the pattern if the first 'i' characters 
    of 'binary' are identical to the first 'i' characters of 'pattern', 
    and the 'i'-th character of 'binary' is '1'.

    Args:
        pattern: The target binary pattern string.
        binary: The binary string to check against the pattern.

    Returns:
        The number of times the prefix-aligned condition is met.

    Examples:
        >>> solve("111", "10111")
        2
        >>> solve("1011", "10011")
        1
    """
    count = 0
    pattern_length = len(pattern)
    binary_length = len(binary)
    
    # We only need to iterate up to the length of the pattern
    # because the prefix cannot be longer than the pattern itself.
    for i in range(pattern_length):
        # Check if the current character in the binary string is '1'
        # This is the condition that defines a "prefix-aligned" match.
        if binary[i] == '1':
            # Check if the prefix of length (i + 1) matches the pattern.
            # We compare the substring of 'binary' up to i+1 with the 
            # substring of 'pattern' up to i+1.
            if binary[:i + 1] == pattern[:i + 1]:
                count += 1
                
    return count
