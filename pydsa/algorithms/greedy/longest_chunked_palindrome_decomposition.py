METADATA = {
    "id": 1147,
    "name": "Longest Chunked Palindrome Decomposition",
    "slug": "longest_chunked_palindrome_decomposition",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "two_pointer", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n^2) in worst case for string slicing, or O(n) with rolling hash",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of chunks such that the sequence of chunks forms a palindrome.",
}

def solve(text: str) -> int:
    """
    Finds the maximum number of chunks in a chunked palindrome decomposition.
    
    The algorithm uses a greedy approach: find the smallest prefix that matches 
    the smallest suffix, count them as two chunks, and then recurse on the 
    remaining inner string.

    Args:
        text: The input string to decompose.

    Returns:
        The maximum number of chunks in the decomposition.

    Examples:
        >>> solve("ghiabcdefghi")
        3
        >>> solve("aaaaa")
        5
        >>> solve("ghiabcdeffedcbazghi")
        7
    """
    if not text:
        return 0

    n = len(text)
    # We iterate through possible lengths of the prefix/suffix chunks
    # starting from length 1 up to half the length of the current string.
    for length in range(1, (n // 2) + 1):
        prefix = text[:length]
        suffix = text[n - length:]

        # Greedy choice: the first time we find a matching prefix and suffix,
        # we take them. This is optimal because taking a larger chunk would 
        # only reduce the total number of chunks possible.
        if prefix == suffix:
            # We found 2 chunks (prefix and suffix) and recurse on the middle part.
            return 2 + solve(text[length : n - length])

    # If no matching prefix and suffix are found, the entire string is one chunk.
    return 1
