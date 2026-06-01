METADATA = {
    "id": 893,
    "name": "Groups of Special-Equivalent Strings",
    "slug": "groups-of-special-equivalent-strings",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash table", "string", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n * k log k)",
    "space_complexity": "O(n * k)",
    "description": "Group strings that are special-equivalent based on the sorted characters at even and odd indices.",
}

def solve(arr: list[str]) -> int:
    """
    Groups special-equivalent strings and returns the number of unique groups.

    Two strings are special-equivalent if the sorted characters at their even 
    indices are identical and the sorted characters at their odd indices 
    are identical.

    Args:
        arr: A list of strings to be grouped.

    Returns:
        The number of unique groups of special-equivalent strings.

    Examples:
        >>> solve(["addee", "daeed", "ddeea"])
        1
        >>> solve(["abcd", "dbca", "bacd"])
        3
    """
    # A set to store the unique "fingerprints" of the special-equivalent groups
    unique_groups = set()

    for string in arr:
        even_chars = []
        odd_chars = []

        # Separate characters based on their index parity
        for index, char in enumerate(string):
            if index % 2 == 0:
                even_chars.append(char)
            else:
                odd_chars.append(char)

        # Sort both lists to create a canonical representation (fingerprint)
        # The fingerprint is a tuple of the sorted even characters and sorted odd characters
        even_chars.sort()
        odd_chars.sort()
        
        # Using a tuple as a key because it is hashable and can be stored in a set
        fingerprint = (tuple(even_chars), tuple(odd_chars))
        unique_groups.add(fingerprint)

    return len(unique_groups)
