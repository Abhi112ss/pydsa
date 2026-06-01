METADATA = {
    "id": 3042,
    "name": "Count Prefix and Suffix Pairs I",
    "slug": "count-prefix-and-suffix-pairs-i",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "brute_force"],
    "difficulty": "easy",
    "time_complexity": "O(n^2 * m)",
    "space_complexity": "O(1)",
    "description": "Count the number of pairs (i, j) such that words[i] is both a prefix and a suffix of words[j].",
}

def solve(words: list[str]) -> int:
    """
    Counts the number of pairs (i, j) where words[i] is both a prefix and a suffix of words[j].

    Args:
        words: A list of strings to evaluate.

    Returns:
        The total count of valid pairs (i, j) where i < j.

    Examples:
        >>> solve(["a", "ab", "a"])
        2
        >>> solve(["c", "ca", "cb", "ca"])
        2
    """
    count = 0
    n = len(words)

    # Iterate through every possible pair (i, j) where i < j
    for i in range(n):
        prefix_candidate = words[i]
        candidate_len = len(prefix_candidate)
        
        for j in range(i + 1, n):
            target_word = words[j]
            target_len = len(target_word)
            
            # A word can only be a prefix/suffix if it is not longer than the target
            if candidate_len <= target_len:
                # Check if the candidate matches the start and end of the target word
                # Using slicing is efficient for small to medium string lengths
                is_prefix = target_word.startswith(prefix_candidate)
                is_suffix = target_word.endswith(prefix_candidate)
                
                if is_prefix and is_suffix:
                    count += 1
                    
    return count
