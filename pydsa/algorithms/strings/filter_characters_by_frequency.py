METADATA = {
    "id": 3662,
    "name": "Filter Characters by Frequency",
    "slug": "filter_characters_by_frequency",
    "category": "Strings",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Filter a string to keep only characters that appear at least a certain number of times.",
}

def solve(s: str, min_frequency: int) -> str:
    """
    Filters the input string to include only characters that appear 
    with a frequency greater than or equal to the specified threshold.

    Args:
        s: The input string to be filtered.
        min_frequency: The minimum required frequency for a character to be kept.

    Returns:
        A new string containing only the characters from the original string 
        that meet the frequency requirement, preserving their original order.

    Examples:
        >>> solve("aabbccdde", 2)
        'aabbccdd'
        >>> solve("apple", 2)
        'pp'
        >>> solve("abcde", 1)
        'abcde'
    """
    if not s:
        return ""

    # Step 1: Build a frequency map of all characters in the string
    frequency_map: dict[str, int] = {}
    for char in s:
        frequency_map[char] = frequency_map.get(char, 0) + 1

    # Step 2: Construct the result string by checking the frequency map
    # We iterate through the original string to maintain the relative order
    result_chars: list[str] = []
    for char in s:
        if frequency_map[char] >= min_frequency:
            result_chars.append(char)

    return "".join(result_chars)
