METADATA = {
    "id": 3076,
    "name": "Shortest Uncommon Substring in an Array",
    "slug": "shortest-uncommon-substring-in-an-array",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "hash_map", "substring"],
    "difficulty": "medium",
    "time_complexity": "O(n * m^3)",
    "space_complexity": "O(n * m^2)",
    "description": "Find the length of the shortest substring of any string in the array that does not appear as a substring in any other string in the array.",
}

def solve(words: list[str]) -> int:
    """
    Finds the length of the shortest substring that is unique to one string in the array.

    Args:
        words: A list of strings.

    Returns:
        The length of the shortest uncommon substring. Returns -1 if no such substring exists.

    Examples:
        >>> solve(["a", "ba", "ca"])
        1
        >>> solve(["a", "aa", "aaa"])
        -1
        >>> solve(["abc", "def", "ghi"])
        1
    """
    n = len(words)
    # We want to find the minimum length, so we iterate through possible lengths 1 to max_len
    max_len = max(len(word) for word in words)

    for length in range(1, max_len + 1):
        # For each length, we check every word to see if it contains a unique substring of that length
        for i in range(n):
            current_word = words[i]
            if len(current_word) < length:
                continue

            # Extract all substrings of the current 'length' from the current word
            # We use a set to avoid checking the same substring multiple times for the same word
            seen_in_current = set()
            for start in range(len(current_word) - length + 1):
                substring = current_word[start : start + length]
                if substring in seen_in_current:
                    continue
                seen_in_current.add(substring)

                # Check if this substring exists in any OTHER word in the array
                is_unique = True
                for j in range(n):
                    if i == j:
                        continue
                    if substring in words[j]:
                        is_unique = False
                        break
                
                # If we found a unique substring of the current length, it is guaranteed 
                # to be the shortest because we are iterating length from 1 upwards.
                if is_unique:
                    return length

    return -1
