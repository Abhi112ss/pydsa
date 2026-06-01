METADATA = {
    "id": 2157,
    "name": "Groups of Strings",
    "slug": "groups-of-strings",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n * k log k)",
    "space_complexity": "O(n * k)",
    "description": "Group strings that are anagrams of each other into lists.",
}

def solve(words: list[str]) -> list[list[str]]:
    """
    Groups strings that are anagrams of each other.

    Args:
        words: A list of strings to be grouped.

    Returns:
        A list of lists, where each sub-list contains strings that are anagrams.

    Examples:
        >>> solve(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    # Dictionary to map the sorted version of a string (canonical form) 
    # to the list of original strings that form that anagram group.
    anagram_groups: dict[str, list[str]] = {}

    for word in words:
        # Sorting the characters of the word provides a unique key 
        # for all strings that are anagrams of each other.
        sorted_key = "".join(sorted(word))
        
        if sorted_key not in anagram_groups:
            anagram_groups[sorted_key] = []
        
        # Append the original word to its corresponding anagram group.
        anagram_groups[sorted_key].append(word)

    # Return all the grouped lists collected in the dictionary values.
    return list(anagram_groups.values())
