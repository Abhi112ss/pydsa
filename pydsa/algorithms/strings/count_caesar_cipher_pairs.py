METADATA = {
    "id": 3805,
    "name": "Count Caesar Cipher Pairs",
    "slug": "count_caesar_cipher_pairs",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Count pairs of strings that are Caesar cipher shifts of each other by comparing their character difference sequences.",
}

def solve(words: list[str]) -> int:
    """
    Counts the number of pairs (i, j) such that words[i] is a Caesar cipher 
    shift of words[j]. Two strings are Caesar cipher shifts if they have 
    the same length and the difference between corresponding characters 
    is constant modulo 26.

    Args:
        words: A list of strings to analyze.

    Returns:
        The total number of pairs (i, j) with i < j that satisfy the condition.

    Examples:
        >>> solve(["abc", "bcd", "xyz"])
        2
        >>> solve(["a", "b", "c"])
        3
        >>> solve(["abc", "def", "ghi"])
        3
    """
    # A dictionary to store the frequency of "normalized" forms.
    # The key will be a tuple representing the relative differences 
    # between adjacent characters and the length of the string.
    # To handle single-character strings, we use a special marker.
    signature_counts: dict[tuple[int, ...], int] = {}
    total_pairs = 0

    for word in words:
        n = len(word)
        
        # If the word is a single character, its "signature" is just its length.
        # Any single character string is a Caesar shift of any other single character string.
        if n == 1:
            signature = (1,)
        else:
            # Calculate the sequence of differences between adjacent characters modulo 26.
            # For a Caesar cipher, this sequence must be identical for both strings.
            # We also include the length in the signature to ensure strings of 
            # different lengths aren't matched.
            diffs = []
            for i in range(n - 1):
                diff = (ord(word[i + 1]) - ord(word[i])) % 26
                diffs.append(diff)
            signature = (n, *tuple(diffs))

        # If this signature has been seen before, every previous occurrence 
        # forms a valid pair with the current word.
        count = signature_counts.get(signature, 0)
        total_pairs += count
        
        # Update the frequency of this signature.
        signature_counts[signature] = count + 1

    return total_pairs
