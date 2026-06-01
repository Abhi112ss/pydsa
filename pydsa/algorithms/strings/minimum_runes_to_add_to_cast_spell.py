METADATA = {
    "id": 3383,
    "name": "Minimum Runes to Add to Cast Spell",
    "slug": "minimum-runes-to-add-to-cast-spell",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of runes to add to a sequence to make it contain a specific target subsequence.",
}

def solve(runes: str, target: str) -> int:
    """
    Calculates the minimum number of runes that need to be added to the 
    'runes' string to ensure the 'target' string appears as a subsequence.

    Args:
        runes: A string representing the available runes.
        target: A string representing the required sequence of runes.

    Returns:
        The minimum number of runes to add.

    Examples:
        >>> solve("abc", "def")
        3
        >>> solve("ace", "abcde")
        2
        >>> solve("aaaaa", "aa")
        0
    """
    target_len = len(target)
    runes_len = len(runes)
    
    target_index = 0
    
    # Iterate through the available runes to find matches for the target sequence
    for rune in runes:
        # If we have already matched all runes in the target, we can stop
        if target_index == target_len:
            break
            
        # If the current rune matches the next required rune in the target
        if rune == target[target_index]:
            target_index += 1
            
    # The number of runes to add is the number of target runes we failed to find
    # in the correct relative order within the existing runes string.
    return target_len - target_index
