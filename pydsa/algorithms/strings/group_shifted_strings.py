METADATA = {
    "id": 249,
    "name": "Group Shifted Strings",
    "slug": "group_shifted_strings",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Groups strings that belong to the same shifting sequence.",
}

def solve(strings: list[str]) -> list[list[str]]:
    """
    Groups strings into lists where each list contains strings that are 
    shifts of each other.

    Args:
        strings: A list of strings to be grouped.

    Returns:
        A list of lists, where each inner list contains strings belonging 
        to the same shifting sequence.

    Examples:
        >>> solve(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
        [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]
    """
    groups: dict[tuple[int, ...], list[str]] = {}

    for s in strings:
        # If string is single char, its pattern is empty or constant
        if len(s) == 0:
            key = ()
        else:
            # Calculate the relative difference between consecutive characters.
            # We use (char[i] - char[i-1]) % 26 to handle wrap-around (e.g., 'az' and 'ba').
            # This creates a unique signature for any shifted sequence.
            differences = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                differences.append(diff)
            key = tuple(differences)

        # Group strings by their calculated difference pattern
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    return list(groups.values())
