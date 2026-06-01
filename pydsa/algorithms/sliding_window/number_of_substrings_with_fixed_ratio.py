METADATA = {
    "id": 2489,
    "name": "Number of Substrings With Fixed Ratio",
    "slug": "number-of-substrings-with-fixed-ratio",
    "category": "Hash Map",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of substrings where the ratio of the count of character 'a' to character 'b' is exactly equal to a given ratio.",
}

def solve(s: str, a_count: int, b_count: int) -> int:
    """
    Calculates the number of substrings where the ratio of 'a's to 'b's 
    is exactly a_count : b_count.

    The problem can be transformed into finding substrings where:
    count_a / count_b = a_count / b_count
    => count_a * b_count = count_b * a_count
    => count_a * b_count - count_b * a_count = 0

    Args:
        s: The input string consisting of 'a' and 'b'.
        a_count: The required count of 'a' in the ratio.
        b_count: The required count of 'b' in the ratio.

    Returns:
        The total number of substrings satisfying the ratio.

    Examples:
        >>> solve("aabb", 1, 1)
        3
        >>> solve("ababa", 1, 1)
        4
    """
    # The target is to find substrings where (count_a * b_count) - (count_b * a_count) == 0
    # Let val = (running_a * b_count) - (running_b * a_count)
    # We want to find pairs of indices (i, j) such that val[j] - val[i] == 0
    
    # count_map stores the frequency of the 'val' encountered so far
    # Initialize with 0: 1 to handle substrings starting from index 0
    count_map: dict[int, int] = {0: 1}
    
    current_a_count = 0
    current_b_count = 0
    total_substrings = 0
    
    for char in s:
        if char == 'a':
            current_a_count += 1
        else:
            current_b_count += 1
            
        # Calculate the current transformed value based on the ratio formula
        # This value represents the 'balance' relative to the target ratio
        current_val = (current_a_count * b_count) - (current_b_count * a_count)
        
        # If this balance has been seen before, it means the substring between 
        # the previous occurrence and now satisfies the ratio.
        if current_val in count_map:
            total_substrings += count_map[current_val]
            count_map[current_val] += 1
        else:
            count_map[current_val] = 1
            
    return total_substrings
