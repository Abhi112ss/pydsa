METADATA = {
    "id": 2379,
    "name": "Minimum Recolors to Get K Consecutive Black Blocks",
    "slug": "minimum_recolors_to_get_k_consecutive_black_blocks",
    "category": "string",
    "aliases": [],
    "tags": ["sliding_window", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of recolors needed to obtain k consecutive black blocks in a binary string.",
}


def solve(s: str, k: int) -> int:
    """Return the minimum number of recolors required to get k consecutive black blocks.

    Args:
        s: A string consisting only of characters 'B' (black) and 'W' (white).
        k: The length of the desired consecutive black block segment.

    Returns:
        The smallest number of white blocks that must be recolored to black
        within any substring of length k.

    Examples:
        >>> solve("WBBWWBBWBW", 7)
        3
        >>> solve("BBBB", 3)
        0
        >>> solve("WWWW", 2)
        2
    """
    # Count white blocks in the first window of size k
    white_count = sum(1 for char in s[:k] if char == 'W')
    min_recolors = white_count

    # Slide the window across the string, updating the white count incrementally
    for right_index in range(k, len(s)):
        left_char = s[right_index - k]
        new_char = s[right_index]

        if left_char == 'W':
            white_count -= 1  # leaving white block
        if new_char == 'W':
            white_count += 1  # entering white block

        if white_count < min_recolors:
            min_recolors = white_count

    return min_recolors