METADATA = {
    "id": 1023,
    "name": "Camelcase Matching",
    "slug": "camelcase-matching",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string"],
    "difficulty": "medium",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(1)",
    "description": "Determine if a query string matches a pattern string according to Camelcase rules.",
}

def solve(pattern: str, query: str) -> bool:
    """
    Determines if the query string matches the pattern string based on Camelcase rules.
    
    Rules:
    1. The pattern must be a subsequence of the query.
    2. All uppercase characters in the query must be present in the pattern.
    3. The characters in the pattern must match the characters in the query in order.

    Args:
        pattern: The Camelcase pattern to match against.
        query: The string to be checked.

    Returns:
        True if the query matches the pattern, False otherwise.

    Examples:
        >>> solve("WaterBottle", "WaterBottleIsGreat")
        True
        >>> solve("Dog", "dog")
        False
        >>> solve("Dog", "CatsAndDogs")
        False
    """
    pattern_index = 0
    query_index = 0
    
    pattern_len = len(pattern)
    query_len = len(query)

    while query_index < query_len:
        # If characters match, move both pointers forward
        if pattern_index < pattern_len and query[query_index] == pattern[pattern_index]:
            pattern_index += 1
            query_index += 1
        # If the query character is uppercase but doesn't match the current pattern char,
        # it violates the rule that all uppercase chars in query must be in pattern.
        elif query[query_index].isupper():
            return False
        else:
            # Otherwise, just move the query pointer forward (skipping lowercase chars)
            query_index += 1

    # The pattern is a valid match only if we have exhausted all characters in the pattern
    return pattern_index == pattern_len
