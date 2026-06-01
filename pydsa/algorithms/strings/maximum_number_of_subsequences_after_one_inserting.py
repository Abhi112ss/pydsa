METADATA = {
    "id": 3628,
    "name": "Maximum Number of Subsequences After One Inserting",
    "slug": "maximum-number-of-subsequences-after-one-inserting",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "greedy", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of subsequences of a specific character that can be formed by inserting one character into a string.",
}

def solve(s: str, char: str) -> int:
    """
    Args:
        s: The input string.
        char: The character to be inserted.

    Returns:
        The maximum number of subsequences of 'char' possible after one insertion.
    """
    count_char = 0
    for current_char in s:
        if current_char == char:
            count_char += 1

    total_subsequences = 0
    current_running_count = 0
    for current_char in s:
        if current_char == char:
            total_subsequences += current_running_count
            current_running_count += 1

    max_additional = 0
    prefix_count = 0
    for current_char in s:
        if current_char == char:
            prefix_count += 1
    
    suffix_count = 0
    for current_char in reversed(s):
        if current_char == char:
            suffix_count += 1

    option_start = suffix_count
    option_end = prefix_count

    return total_subsequences + max(option_start, option_end)