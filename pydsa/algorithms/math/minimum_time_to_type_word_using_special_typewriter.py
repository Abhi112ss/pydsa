METADATA = {
    "id": 1974,
    "name": "Minimum Time to Type Word Using Special Typewriter",
    "slug": "minimum_time_to_type_word_using_special_typewriter",
    "category": "string",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate minimal time to type a word on a circular typewriter.",
}


def solve(word: str) -> int:
    """Calculate the minimum time required to type a given word using a special typewriter.

    The typewriter has 26 lowercase English letters arranged in a circle.
    Starting from the pointer at 'a', moving the pointer one step clockwise or
    counter‑clockwise costs 1 unit of time, and pressing a key costs 0 time.

    Args:
        word: The target word consisting of lowercase English letters.

    Returns:
        The minimum total time to type the entire word.

    Examples:
        >>> solve("abc")
        2
        >>> solve("bza")
        4
    """
    total_time: int = 0
    current_char: str = 'a'

    for target_char in word:
        # Compute direct distance between current and target characters
        direct_distance: int = abs(ord(target_char) - ord(current_char))
        # Choose the shorter path around the circular alphabet
        minimal_distance: int = min(direct_distance, 26 - direct_distance)
        total_time += minimal_distance
        current_char = target_char

    return total_time