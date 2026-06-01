METADATA = {
    "id": 3498,
    "name": "Reverse Degree of a String",
    "slug": "reverse_degree_of_a_string",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "math", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Transform a string based on the reverse frequency of its characters.",
}

def solve(s: str) -> str:
    """
    Transforms a string by replacing each character with a new character 
    based on the reverse order of character frequencies.

    The transformation logic:
    1. Count the frequency of each character.
    2. Sort characters primarily by frequency (descending) and secondarily by character (ascending).
    3. Map the original characters to the characters in this sorted list in reverse order.

    Args:
        s: The input string to be transformed.

    Returns:
        The transformed string.

    Examples:
        >>> solve("aabbcc")
        'ccbbaa'
        >>> solve("apple")
        'eppla'
    """
    if not s:
        return ""

    # Step 1: Calculate character frequencies
    frequencies: dict[str, int] = {}
    for char in s:
        frequencies[char] = frequencies.get(char, 0) + 1

    # Step 2: Create a sorted list of unique characters.
    # We sort by frequency descending, then by character ascending to ensure stability.
    # This defines the "degree" order.
    unique_chars = sorted(
        frequencies.keys(), 
        key=lambda char: (-frequencies[char], char)
    )

    # Step 3: Create the mapping.
    # The problem asks for the "reverse degree", meaning the character at index i 
    # in the sorted list maps to the character at index (N-1-i).
    mapping: dict[str, str] = {}
    n = len(unique_chars)
    for i in range(n):
        mapping[unique_chars[i]] = unique_chars[n - 1 - i]

    # Step 4: Construct the result string using the mapping
    result_chars: list[str] = []
    for char in s:
        result_chars.append(mapping[char])

    return "".join(result_chars)
