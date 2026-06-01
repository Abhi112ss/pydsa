METADATA = {
    "id": 1081,
    "name": "Smallest Subsequence of Distinct Characters",
    "slug": "smallest-subsequence-of-distinct-characters",
    "category": "String",
    "aliases": ["Remove Duplicate Letters"],
    "tags": ["monotonic_stack", "greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the lexicographically smallest subsequence of a string that contains all the distinct characters of the original string exactly once.",
}

def solve(s: str) -> str:
    """
    Finds the lexicographically smallest subsequence containing all distinct characters.

    Args:
        s: The input string.

    Returns:
        The lexicographically smallest subsequence of distinct characters.

    Examples:
        >>> solve("bcabc")
        'abc'
        >>> solve("cbacdcbc")
        'acdb'
    """
    # Count the frequency of each character to know if we can discard it later
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    # Track characters currently in our result stack to ensure uniqueness
    visited = set()
    stack = []

    for index, char in enumerate(s):
        # If character is already in our subsequence, skip it to maintain uniqueness
        if char in visited:
            continue

        # While:
        # 1. Stack is not empty
        # 2. Current char is smaller than the top of the stack (greedy choice)
        # 3. The top char of the stack appears again later in the string (safety check)
        while stack and char < stack[-1] and last_occurrence[stack[-1]] > index:
            removed_char = stack.pop()
            visited.remove(removed_char)

        # Add the current character to the stack and mark as visited
        stack.append(char)
        visited.add(char)

    return "".join(stack)
