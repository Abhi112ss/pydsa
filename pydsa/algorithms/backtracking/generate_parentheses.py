METADATA = {
    "id": 22,
    "name": "Generate Parentheses",
    "slug": "generate-parentheses",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "strings", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(4^n / sqrt(n))",
    "space_complexity": "O(n)",
    "description": "Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.",
}

def solve(n: int) -> list[str]:
    """
    Generates all combinations of well-formed parentheses using backtracking.

    Args:
        n: The number of pairs of parentheses.

    Returns:
        A list of strings containing all valid combinations of n pairs of parentheses.

    Examples:
        >>> solve(3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
    """
    result: list[str] = []

    def backtrack(current_string: str, open_count: int, close_count: int) -> None:
        """
        A recursive helper function to build valid parentheses strings.

        Args:
            current_string: The string built so far.
            open_count: The number of opening parentheses used.
            close_count: The number of closing parentheses used.
        """
        # Base case: if the current string length reaches 2 * n, it is a valid combination
        if len(current_string) == 2 * n:
            result.append(current_string)
            return

        # If we can still add an opening parenthesis, do so
        if open_count < n:
            backtrack(current_string + "(", open_count + 1, close_count)

        # If we can add a closing parenthesis (must be fewer than opening to be valid)
        if close_count < open_count:
            backtrack(current_string + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result
