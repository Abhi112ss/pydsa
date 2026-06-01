METADATA = {
    "id": 3137,
    "name": "Minimum Number of Operations to Make Word K-Periodic",
    "slug": "minimum-number-of-operations-to-make-word-k-periodic",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the minimum number of character changes to make a word k-periodic by ensuring characters at indices i, i+k, i+2k... are identical.",
}

def solve(word: str, k: int) -> int:
    """
    Calculates the minimum number of operations to make the word k-periodic.
    
    A word is k-periodic if word[i] == word[i + k] for all valid i.
    To minimize operations, for each position in the period [0, k-1], 
    we identify the most frequent character among all characters that 
    occupy that position in the periodic sequence and change all others to it.

    Args:
        word: The input string to be transformed.
        k: The period length.

    Returns:
        The minimum number of character changes required.

    Examples:
        >>> solve("ababc", 2)
        2
        >>> solve("letcode", 3)
        2
    """
    n = len(word)
    total_operations = 0

    # Iterate through each position in the period of length k
    for start_index in range(k):
        char_counts: dict[str, int] = {}
        total_chars_in_group = 0
        
        # Traverse the string in steps of k to collect characters in the same periodic group
        for i in range(start_index, n, k):
            char = word[i]
            char_counts[char] = char_counts.get(char, 0) + 1
            total_chars_in_group += 1
        
        # Find the frequency of the most common character in this group
        # To minimize changes, we keep the most frequent character and change the rest
        max_freq = 0
        if char_counts:
            max_freq = max(char_counts.values())
            
        # The number of operations for this group is (total elements in group - frequency of most common)
        total_operations += (total_chars_in_group - max_freq)

    return total_operations
