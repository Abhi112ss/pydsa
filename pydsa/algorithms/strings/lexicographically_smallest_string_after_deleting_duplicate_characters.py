METADATA = {
    "id": 3816,
    "name": "Lexicographically Smallest String After Deleting Duplicate Characters",
    "slug": "lexicographically-smallest-string-after-deleting-duplicate-characters",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "greedy", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the lexicographically smallest string possible by deleting duplicate characters such that every unique character remains exactly once.",
}

def solve(s: str) -> str:
    """
    Finds the lexicographically smallest string containing all unique characters from s.

    Args:
        s: The input string.

    Returns:
        The lexicographically smallest string containing each unique character exactly once.

    Examples:
        >>> solve("cbacdcbc")
        'acdb'
        >>> solve("bcabc")
        'abc'
    """
    # Count the frequency of each character to know if we can delete it later
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Keep track of characters currently in our monotonic stack
    visited = set()
    stack = []

    for char in s:
        # Decrement the count of the current character as we process it
        char_counts[char] -= 1

        # If the character is already in our result, skip it to maintain uniqueness
        if char in visited:
            continue

        # Monotonic stack logic:
        # While the stack is not empty, the current char is smaller than the top,
        # AND the top char appears again later in the string (count > 0),
        # pop the top char to allow for a lexicographically smaller sequence.
        while stack and char < stack[-1] and char_counts[stack[-1]] > 0:
            removed_char = stack.pop()
            visited.remove(removed_char)

        # Add the current character to the stack and mark as visited
        stack.append(char)
        visited.add(char)

    return "".join(stack)
