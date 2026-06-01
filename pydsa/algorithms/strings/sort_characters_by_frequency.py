METADATA = {
    "id": 451,
    "name": "Sort Characters By Frequency",
    "slug": "sort-characters-by-frequency",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "sorting", "heap", "bucket_sort"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Sort a string in decreasing order based on the frequency of the characters.",
}

def solve(s: str) -> str:
    """
    Sorts the characters in a string based on their frequency in descending order.
    
    Uses the Bucket Sort algorithm to achieve linear time complexity.
    
    Args:
        s: The input string to be sorted.
        
    Returns:
        A string where characters are ordered by their frequency.
        
    Examples:
        >>> solve("tree")
        'eert'
        >>> solve("cccaaa")
        'cccaaa'
        >>> solve("Aabb")
        'bbAa'
    """
    if not s:
        return ""

    # Step 1: Count the frequency of each character
    frequencies: dict[str, int] = {}
    for char in s:
        frequencies[char] = frequencies.get(char, 0) + 1

    # Step 2: Use Bucket Sort approach
    # Create buckets where the index represents the frequency
    # The maximum possible frequency is len(s)
    buckets: list[list[str]] = [[] for _ in range(len(s) + 1)]
    for char, count in frequencies.items():
        buckets[count].append(char)

    # Step 3: Build the result string by iterating through buckets from highest to lowest
    result_parts: list[str] = []
    for frequency in range(len(s), 0, -1):
        for char in buckets[frequency]:
            # Append the character multiplied by its frequency
            result_parts.append(char * frequency)

    return "".join(result_parts)
