METADATA = {
    "id": 186,
    "name": "Reverse Words in a String II",
    "slug": "reverse_words_in_a_string_ii",
    "category": "Algorithms",
    "aliases": [],
    "tags": ["two_pointer", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reverse the order of words in a character array in-place.",
}


def solve(s: list[str]) -> None:
    """
    Reverses the order of words in the given character array in-place.

    Args:
        s: A list of characters representing a string of words separated by spaces.

    Returns:
        None: The modification is performed in-place.

    Examples:
        >>> chars = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        >>> solve(chars)
        >>> chars
        ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    """

    def reverse_range(arr: list[str], left: int, right: int) -> None:
        """Helper to reverse a portion of the array in-place."""
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Step 1: Reverse the entire array
    # This puts the words in the correct order relative to each other,
    # but each individual word is reversed.
    reverse_range(s, 0, len(s) - 1)

    # Step 2: Reverse each individual word back to its original character order
    word_start = 0
    for current_index in range(len(s) + 1):
        # Check if we reached the end of a word or the end of the array
        if current_index == len(s) or s[current_index] == " ":
            # Reverse the word found between word_start and current_index - 1
            reverse_range(s, word_start, current_index - 1)
            # Move the start pointer to the beginning of the next word
            word_start = current_index + 1

    return None