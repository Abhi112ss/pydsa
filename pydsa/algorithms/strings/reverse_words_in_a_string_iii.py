METADATA = {
    "id": 557,
    "name": "Reverse Words in a String III",
    "slug": "reverse_words_in_a_string_iii",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reverse each word in a string while preserving word order.",
}


def solve(s: str) -> str:
    """Reverse each word in the input string while preserving the original word order.

    Args:
        s: A string consisting of words separated by single spaces.

    Returns:
        A new string where each word is reversed but the sequence of words remains unchanged.

    Examples:
        >>> solve("Let's take LeetCode contest")
        "s'teL ekat edoCteeL tsetnoc"
        >>> solve("God Ding")
        "doG gniD"
    """
    # Convert the string to a mutable list of characters.
    chars = list(s)
    start_index = 0
    total_length = len(chars)

    while start_index < total_length:
        # Locate the end of the current word (space or end of string).
        end_index = start_index
        while end_index < total_length and chars[end_index] != ' ':
            end_index += 1

        # Reverse the characters of the identified word in place.
        left, right = start_index, end_index - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        # Move to the start of the next word (skip the space).
        start_index = end_index + 1

    return ''.join(chars)