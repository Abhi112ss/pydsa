METADATA = {
    "id": 1324,
    "name": "Print Words Vertically",
    "slug": "print-words-vertically",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N * M)",
    "description": "Given an array of strings, print them vertically by aligning characters at the same index.",
}

def solve(words: list[str]) -> list[str]:
    """
    Transforms an array of words into a vertical representation.

    Args:
        words: A list of strings to be printed vertically.

    Returns:
        A list of strings where each string represents a row in the vertical alignment.

    Examples:
        >>> solve(["abc", "de"])
        ['ad', 'be', 'c ']
        >>> solve(["a", "b", "c"])
        ['abc']
    """
    if not words:
        return []

    # Find the length of the longest word to determine how many rows we need
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)

    result = []

    # Iterate through each character index up to the maximum word length
    for i in range(max_len):
        current_row_chars = []
        for word in words:
            # If the current word has a character at this index, add it
            if i < len(word):
                current_row_chars.append(word[i])
            else:
                # Otherwise, pad with a space to maintain vertical alignment
                current_row_chars.append(" ")
        
        # Join the characters to form the row string
        row_str = "".join(current_row_chars)
        
        # Trim trailing spaces as per problem requirements
        result.append(row_str.rstrip())

    return result
