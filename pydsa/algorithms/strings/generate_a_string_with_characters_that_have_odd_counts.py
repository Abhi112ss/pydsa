METADATA = {
    "id": 1374,
    "name": "Generate a String With Characters That Have Odd Counts",
    "slug": "generate-a-string-with-characters-that-have-odd-counts",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a string where each character appears an odd number of times based on the input string's character frequencies.",
}

def solve(s: str) -> str:
    """
    Generates a string where each character from the input string appears 
    an odd number of times.

    Args:
        s: The input string containing characters.

    Returns:
        A string where each unique character from 's' appears an odd number of times.

    Examples:
        >>> solve("abc")
        'abc'
        >>> solve("aabbcc")
        'abc'
        >>> solve("aaabbb")
        'aaabbb'
    """
    # Step 1: Count the frequency of each character
    char_counts: dict[str, int] = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    result_chars: list[str] = []

    # Step 2: Iterate through the frequency map
    for char, count in char_counts.items():
        # If the count is already odd, we can use the full count.
        # If the count is even, we subtract 1 to make it odd.
        # Note: Since the input string has at least one of each char, 
        # count - 1 will be at least 0. However, if count is even, 
        # count - 1 is at least 1 (since even numbers >= 2).
        if count % 2 == 0:
            actual_count = count - 1
        else:
            actual_count = count
        
        # Append the character 'actual_count' times to our list
        result_chars.append(char * actual_count)

    # Step 3: Join the list into a single string
    return "".join(result_chars)
