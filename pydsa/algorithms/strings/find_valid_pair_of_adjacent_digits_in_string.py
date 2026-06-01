METADATA = {
    "id": 3438,
    "name": "Find Valid Pair of Adjacent Digits in String",
    "slug": "find-valid-pair-of-adjacent-digits-in-string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the first pair of adjacent digits in a string that satisfy specific equality or difference conditions.",
}

def solve(s: str, k: int) -> list[int]:
    """
    Finds the first pair of adjacent digits in the string that satisfy the condition.
    
    The condition for a valid pair (s[i], s[i+1]) is:
    1. s[i] == s[i+1]
    OR
    2. abs(int(s[i]) - int(s[i+1])) == k

    Args:
        s: The input string containing digits.
        k: The target absolute difference.

    Returns:
        A list containing the indices [i, i+1] of the first valid pair found.
        If no such pair exists, returns an empty list [].

    Examples:
        >>> solve("12345", 1)
        [0, 1]
        >>> solve("13579", 1)
        []
        >>> solve("1122", 2)
        [0, 1]
    """
    # Iterate through the string up to the second to last character
    for i in range(len(s) - 1):
        # Convert adjacent characters to integers for comparison
        digit_a = int(s[i])
        digit_b = int(s[i + 1])

        # Check if digits are equal or if their absolute difference equals k
        if digit_a == digit_b or abs(digit_a - digit_b) == k:
            return [i, i + 1]

    # Return empty list if no valid pair is found after full traversal
    return []
