METADATA = {
    "id": 3365,
    "name": "Rearrange K Substrings to Form Target String",
    "slug": "rearrange_k_substrings_to_form_target_string",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "greedy", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a target string can be formed by rearranging a given set of k substrings.",
}

def solve(target: str, substrings: list[str]) -> bool:
    """
    Determines if the target string can be formed by rearranging the given substrings.
    
    The problem boils down to checking if the total frequency of each character 
    across all substrings matches the frequency of that character in the target string.

    Args:
        target: The target string to be formed.
        substrings: A list of strings that are to be rearranged.

    Returns:
        True if the target can be formed, False otherwise.

    Examples:
        >>> solve("aabb", ["ab", "ab"])
        True
        >>> solve("aabb", ["a", "b", "a"])
        False
        >>> solve("abc", ["c", "b", "a"])
        True
    """
    # If the total length of substrings doesn't match target, it's impossible
    if sum(len(s) for s in substrings) != len(target):
        return False

    target_counts: dict[str, int] = {}
    for char in target:
        target_counts[char] = target_counts.get(char, 0) + 1

    substring_counts: dict[str, int] = {}
    for s in substrings:
        for char in s:
            substring_counts[char] = substring_counts.get(char, 0) + 1

    # The target can be formed if and only if the character counts are identical
    # because we are rearranging the substrings (which preserves character counts).
    return target_counts == substring_counts
