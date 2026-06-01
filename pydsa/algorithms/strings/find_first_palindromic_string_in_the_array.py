METADATA = {
    "id": 2108,
    "name": "Find First Palindromic String in the Array",
    "slug": "find_first_palindromic_string_in_the_array",
    "category": "Array",
    "aliases": [],
    "tags": ["string", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Return the first palindromic string in the array, or an empty string if none exist.",
}


def solve(words: list[str]) -> str:
    """Return the first palindromic string in the given list.

    Args:
        words: A list of lowercase strings.

    Returns:
        The first string that reads the same forward and backward.
        If no such string exists, returns an empty string.

    Examples:
        >>> solve(["abc","car","ada","racecar"])
        'ada'
        >>> solve(["notapalindrome","ab"])
        ''
    """
    for candidate in words:
        left_index = 0
        right_index = len(candidate) - 1
        # Check palindrome using two‑pointer technique
        while left_index < right_index:
            if candidate[left_index] != candidate[right_index]:
                break
            left_index += 1
            right_index -= 1
        else:
            # Loop completed without break → palindrome found
            return candidate
    return ""