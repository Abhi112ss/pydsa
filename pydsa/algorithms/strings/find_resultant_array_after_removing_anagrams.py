METADATA = {
    "id": 2273,
    "name": "Find Resultant Array After Removing Anagrams",
    "slug": "find-resultant-array-after-removing-anagrams",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "sorting", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n * k log k)",
    "space_complexity": "O(n * k)",
    "description": "Remove adjacent strings from an array if they are anagrams of each other.",
}

def solve(words: list[str]) -> list[str]:
    """
    Removes adjacent strings from the list if they are anagrams of each other.

    Args:
        words: A list of strings to process.

    Returns:
        A list of strings containing only the elements that are not 
        anagrams of their immediate predecessor in the original sequence.

    Examples:
        >>> solve(["abba", "baba", "bbaa", "cd", "dc"])
        ['abba', 'cd']
        >>> solve(["cd", "cd"])
        ['cd']
    """
    if not words:
        return []

    result: list[str] = []
    
    # We keep track of the 'canonical' form of the last added word.
    # An anagram's canonical form is its characters sorted alphabetically.
    last_canonical_form: str | None = None

    for word in words:
        # Create a sorted version of the current word to identify its anagram group
        current_canonical_form = "".join(sorted(word))

        # If the current word's sorted form is different from the last added word's 
        # sorted form, it is not an adjacent anagram.
        if current_canonical_form != last_canonical_form:
            result.append(word)
            last_canonical_form = current_canonical_form

    return result
