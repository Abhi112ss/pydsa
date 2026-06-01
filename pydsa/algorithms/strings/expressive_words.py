METADATA = {
    "id": 809,
    "name": "Expressive Words",
    "slug": "expressive-words",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(N * L)",
    "space_complexity": "O(L)",
    "description": "Determine if a word can be formed from a target string by stretching groups of identical characters.",
}

def solve(words: list[str], target: str) -> list[bool]:
    """
    Determines which words in the list can be formed by stretching characters in the word.

    A group of characters in the target can be formed by a group in the word if:
    1. The characters are the same.
    2. The target group size is equal to the word group size, OR
    3. The target group size is greater than the word group size AND the target group size is at least 3.

    Args:
        words: A list of strings to check.
        target: The target string to match against.

    Returns:
        A list of booleans where each element indicates if the corresponding word is expressive.

    Examples:
        >>> solve(["hello", "eelllooo"], "heeeelllooo")
        [False, True]
        >>> solve(["expression", "expressive"], "expressiveee")
        [False, True]
    """
    results = []

    for word in words:
        results.append(is_expressive(word, target))

    return results

def is_expressive(word: str, target: str) -> bool:
    """
    Helper function to check if a single word is expressive relative to the target.
    """
    word_idx = 0
    target_idx = 0
    word_len = len(word)
    target_len = len(target)

    while word_idx < word_len and target_idx < target_len:
        if word[word_idx] != target[target_idx]:
            return False

        char = word[word_idx]
        
        # Count consecutive occurrences in the word
        word_count = 0
        while word_idx < word_len and word[word_idx] == char:
            word_count += 1
            word_idx += 1

        # Count consecutive occurrences in the target
        target_count = 0
        while target_idx < target_len and target[target_idx] == char:
            target_count += 1
            target_idx += 1

        # Validation logic:
        # 1. Target group cannot be smaller than word group.
        # 2. If target group is larger, it must be at least 3 to be a valid 'stretch'.
        if target_count < word_count:
            return False
        if target_count > word_count and target_count < 3:
            return False

    # Both strings must be fully consumed to be a match
    return word_idx == word_len and target_idx == target_len
