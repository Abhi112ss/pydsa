METADATA = {
    "id": 1593,
    "name": "Split a String Into the Max Number of Unique Substrings",
    "slug": "split-a-string-into-the-max-number-of-unique-substrings",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "string", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of unique substrings a given string can be split into.",
}

def solve(s: str) -> int:
    """
    Finds the maximum number of unique substrings that can be formed by splitting the input string.

    Args:
        s: The input string to be split.

    Returns:
        The maximum number of unique substrings possible.

    Examples:
        >>> solve("abab")
        2
        >>> solve("rabbbit")
        3
        >>> solve("abc")
        3
    """
    max_splits = 0
    seen_substrings = set()

    def backtrack(start_index: int, current_count: int) -> None:
        nonlocal max_splits

        # Base case: if we reached the end of the string, update the global maximum
        if start_index == len(s):
            max_splits = max(max_splits, current_count)
            return

        # Try every possible end position for the current substring
        for end_index in range(start_index + 1, len(s) + 1):
            substring = s[start_index:end_index]

            # If the substring is unique, proceed with backtracking
            if substring not in seen_substrings:
                seen_substrings.add(substring)
                
                # Recurse to find the next substring
                backtrack(end_index, current_count + 1)
                
                # Backtrack: remove the substring to explore other possibilities
                seen_substrings.remove(substring)

    backtrack(0, 0)
    return max_splits
