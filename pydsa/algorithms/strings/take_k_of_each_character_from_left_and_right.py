METADATA = {
    "id": 2516,
    "name": "Take K of Each Character From Left and Right",
    "slug": "take-k-of-each-character-from-left-and-right",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of characters to remove from the ends of a string such that at least k of each character present in the string remain.",
}

def solve(s: str, k: int) -> int:
    """
    Args:
        s: The input string.
        k: The minimum number of each character required.

    Returns:
        The minimum number of characters to remove from the ends.
    """
    total_counts = {}
    for char in s:
        total_counts[char] = total_counts.get(char, 0) + 1

    required_chars = []
    for char, count in total_counts.items():
        if count < k:
            return -1
        required_chars.append(char)

    num_unique_chars = len(required_chars)
    n = len(s)
    min_removals = n
    current_window_counts = {}
    satisfied_chars = 0
    left = 0

    for right in range(n):
        char_right = s[right]
        current_window_counts[char_right] = current_window_counts.get(char_right, 0) + 1
        
        if current_window_counts[char_right] == k:
            satisfied_chars += 1

        while satisfied_chars == num_unique_chars:
            min_removals = min(min_removals, n - (right - left + 1))
            
            char_left = s[left]
            if current_window_counts[char_left] == k:
                satisfied_chars -= 1
            current_window_counts[char_left] -= 1
            left += 1

    return min_removals