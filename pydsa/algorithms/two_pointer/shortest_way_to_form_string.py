METADATA = {
    "id": 1055,
    "name": "Shortest Way to Form String",
    "slug": "shortest-way-to-form-string",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "two_pointer"],
    "difficulty": "hard",
    "time_complexity": "O(S * T)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of subsequences of a source string needed to construct a target string.",
}

def solve(source: str, target: str) -> int:
    """
    Finds the minimum number of subsequences of 'source' required to form 'target'.

    The algorithm uses a greedy approach. For each subsequence, we try to match 
    as many characters of the target as possible by iterating through the source.

    Args:
        source: The string used to form the target.
        target: The string to be formed.

    Returns:
        The minimum number of subsequences of source needed to form target. 
        Returns -1 if it is impossible to form the target.

    Examples:
        >>> solve("abc", "abcabc")
        2
        >>> solve("abc", "acb")
        -1
        >>> solve("a", "aaaaa")
        5
    """
    target_index = 0
    target_length = len(target)
    subsequence_count = 0

    while target_index < target_length:
        source_index = 0
        matched_in_this_pass = False

        # Try to match as many characters of target as possible using one pass of source
        while source_index < len(source) and target_index < target_length:
            if source[source_index] == target[target_index]:
                target_index += 1
                matched_in_this_pass = True
            source_index += 1

        # If we couldn't match even a single character in a full pass of source,
        # it means the target contains a character not present in source.
        if not matched_in_this_pass:
            return -1

        # Increment the count of subsequences used
        subsequence_count += 1

    return subsequence_count
