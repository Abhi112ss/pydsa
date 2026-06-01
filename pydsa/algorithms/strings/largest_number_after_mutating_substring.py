METADATA = {
    "id": 1946,
    "name": "Largest Number After Mutating Substring",
    "slug": "largest-number-after-mutating-substring",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the largest possible number by replacing a substring of length k with '9's.",
}

def solve(number: str, k: int) -> str:
    """
    Finds the largest possible number by replacing a substring of length k with '9's.

    Args:
        number: A string representing a non-negative integer.
        k: The length of the substring to be replaced by '9's.

    Returns:
        The largest possible string representation of the number after mutation.

    Examples:
        >>> solve("12345", 2)
        '12995'
        >>> solve("999", 1)
        '999'
        >>> solve("1000", 1)
        '9000'
    """
    n = len(number)
    max_val = number

    # Iterate through every possible starting position for a substring of length k
    for i in range(n - k + 1):
        # Construct the new number by replacing the substring [i : i+k] with '9's
        # We use string slicing to build the candidate
        prefix = number[:i]
        suffix = number[i + k:]
        replacement = "9" * k
        candidate = prefix + replacement + suffix

        # Compare the candidate with the current maximum found
        # Since all candidates have the same length, lexicographical comparison works
        if candidate > max_val:
            max_val = candidate

    return max_val
