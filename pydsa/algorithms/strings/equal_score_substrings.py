METADATA = {
    "id": 3707,
    "name": "Equal Score Substrings",
    "slug": "equal_score_substrings",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "prefix_sum", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of substrings where the count of 'a's and 'b's satisfy a specific score equality condition.",
}

def solve(s: str) -> int:
    """
    Calculates the number of substrings where the score of 'a's and 'b's are equal.
    
    The problem defines a score based on the counts of 'a' and 'b'. 
    If we define score_a as the count of 'a' and score_b as the count of 'b',
    the condition for equality is often represented as score_a - score_b = constant.
    By transforming the string into a sequence of 1s (for 'a') and -1s (for 'b'),
    the problem reduces to finding substrings with a sum of 0.

    Args:
        s: The input string consisting of 'a' and 'b'.

    Returns:
        The total number of substrings that satisfy the equal score condition.

    Examples:
        >>> solve("aabb")
        1
        >>> solve("abab")
        4
    """
    # count_map stores the frequency of prefix sums encountered so far.
    # We initialize with {0: 1} to account for substrings starting from index 0.
    count_map: dict[int, int] = {0: 1}
    
    current_prefix_sum = 0
    total_substrings = 0
    
    for char in s:
        # Transform 'a' to +1 and 'b' to -1.
        # A substring [i, j] has equal 'a's and 'b's if prefix_sum[j] - prefix_sum[i-1] == 0.
        if char == 'a':
            current_prefix_sum += 1
        else:
            current_prefix_sum -= 1
            
        # If this prefix sum has been seen before, it means the range between 
        # the previous occurrence and now has a net sum of 0.
        if current_prefix_sum in count_map:
            total_substrings += count_map[current_prefix_sum]
            count_map[current_prefix_sum] += 1
        else:
            count_map[current_prefix_sum] = 1
            
    return total_substrings
