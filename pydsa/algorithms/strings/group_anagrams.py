METADATA = {
    "id": 49,
    "name": "Group Anagrams",
    "slug": "group-anagrams",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n * k log k)",
    "space_complexity": "O(n * k)",
    "description": "Given an array of strings, group the anagrams together.",
}

def solve(strs: list[str]) -> list[list[str]]:
    """
    Groups a list of strings into sub-lists where each sub-list contains anagrams.

    Args:
        strs: A list of strings to be grouped.

    Returns:
        A list of lists, where each inner list contains strings that are anagrams of each other.

    Examples:
        >>> solve(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    # Dictionary to map the sorted version of a string (the canonical form) 
    # to the list of original strings that match that form.
    anagram_map: dict[str, list[str]] = {}

    for word in strs:
        # Sorting the string provides a unique key for all anagrams.
        # For example, 'eat', 'tea', and 'ate' all become 'aet'.
        sorted_key = "".join(sorted(word))
        
        # If the key doesn't exist, initialize a new list.
        if sorted_key not in anagram_map:
            anagram_map[sorted_key] = []
        
        # Append the original word to the list corresponding to its sorted key.
        anagram_map[sorted_key].append(word)

    # Return all the grouped lists from the dictionary values.
    return list(anagram_map.values())
