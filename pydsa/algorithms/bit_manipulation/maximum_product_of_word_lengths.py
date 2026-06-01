METADATA = {
    "id": 318,
    "name": "Maximum Product of Word Lengths",
    "slug": "maximum-product-of-word-lengths",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bitmask", "string", "bit manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 + L)",
    "space_complexity": "O(n)",
    "description": "Find the maximum product of lengths of two words in an array such that the two words do not share any common letters.",
}

def solve(words: list[str]) -> int:
    """
    Calculates the maximum product of lengths of two words that share no common characters.

    Args:
        words: A list of strings representing the words to evaluate.

    Returns:
        The maximum product of lengths of two words with no common characters. 
        Returns 0 if no such pair exists.

    Examples:
        >>> solve(["leet", "code"])
        0
        >>> solve([" всего", "abc", "def", "aaaa"])
        0
        >>> solve(["abc", "def", "aaaa"])
        12
        >>> solve(["apple", "pen", "applepen"])
        0
    """
    # Map to store the maximum length for each unique bitmask.
    # A bitmask represents the set of characters present in a word.
    # Using a dict handles cases where multiple words have the same character set.
    mask_to_max_length: dict[int, int] = {}

    for word in words:
        mask = 0
        for char in word:
            # Create a 26-bit integer where the i-th bit is 1 if the i-th letter is present.
            # ord(char) - ord('a') maps 'a'-'z' to 0-25.
            mask |= 1 << (ord(char) - ord('a'))
        
        # If this bitmask was seen before, we only care about the longest word for it.
        if mask not in mask_to_max_length or len(word) > mask_to_max_length[mask]:
            mask_to_max_length[mask] = len(word)

    max_product = 0
    # Extract unique masks to reduce the number of comparisons in the nested loop.
    unique_masks = list(mask_to_max_length.keys())

    # Compare every pair of unique bitmasks.
    for i in range(len(unique_masks)):
        mask_a = unique_masks[i]
        len_a = mask_to_max_length[mask_a]
        
        for j in range(i + 1, len(unique_masks)):
            mask_b = unique_masks[j]
            
            # If bitwise AND is 0, the two words share no common characters.
            if (mask_a & mask_b) == 0:
                len_b = mask_to_max_length[mask_b]
                max_product = max(max_product, len_a * len_b)

    return max_product
