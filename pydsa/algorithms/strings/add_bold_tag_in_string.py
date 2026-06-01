METADATA = {
    "id": 616,
    "name": "Add Bold Tag in String",
    "slug": "add-bold-tag-in-string",
    "category": "String",
    "aliases": [],
    "tags": ["interval_merging", "string_matching"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n)",
    "description": "Given a string s and a list of substrings, return the string with bold tags applied to all occurrences of the substrings.",
}

def solve(s: str, words: list[str]) -> str:
    """
    Applies bold tags to all occurrences of the given words in the string.

    Args:
        s: The input string.
        words: A list of substrings that should be bolded.

    Returns:
        The string with <b> and </b> tags inserted around bolded segments.

    Examples:
        >>> solve("abc", ["a", "bc"])
        '<b>abc</b>'
        >>> solve("abc", ["ab", "bc"])
        '<b>abc</b>'
        >>> solve("abc", ["a", "c"])
        '<b>a</b>bc<b>c</b>'
    """
    n = len(s)
    # is_bold[i] will be True if character at index i should be bolded
    is_bold = [False] * n

    # Step 1: Mark all characters that belong to any occurrence of any word
    for word in words:
        if not word:
            continue
        word_len = len(word)
        # Find all occurrences of 'word' in 's'
        start_index = s.find(word)
        while start_index != -1:
            # Mark the range [start_index, start_index + word_len)
            for i in range(start_index, start_index + word_len):
                is_bold[i] = True
            # Look for the next occurrence
            start_index = s.find(word, start_index + 1)

    # Step 2: Construct the result string by inserting tags based on is_bold transitions
    result = []
    i = 0
    while i < n:
        if is_bold[i]:
            # Start of a bold segment
            result.append("<b>")
            # Find the end of this continuous bold segment
            while i < n and is_bold[i]:
                result.append(s[i])
                i += 1
            # End of the bold segment
            result.append("</b>")
        else:
            # Regular character
            result.append(s[i])
            i += 1

    return "".join(result)
