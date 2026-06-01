METADATA = {
    "id": 784,
    "name": "Letter Case Permutation",
    "slug": "letter-case-permutation",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["dfs", "recursion", "string", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(2^n * n)",
    "space_complexity": "O(2^n * n)",
    "description": "Given a string s, return all possible permutations of all case variations of s.",
}

def solve(s: str) -> list[str]:
    """
    Generates all possible permutations of case variations for a given string.

    Args:
        s: The input string containing lowercase letters, uppercase letters, or digits.

    Returns:
        A list of strings representing all possible case permutations.

    Examples:
        >>> solve("a1b2")
        ['a1b2', 'a1B2', 'A1b2', 'A1B2']
        >>> solve("3z4")
        ['3z4', '3Z4']
    """
    results: list[str] = []
    # Convert string to list because strings are immutable in Python
    chars: list[str] = list(s)
    n: int = len(chars)

    def backtrack(index: int) -> None:
        """
        Recursive helper to explore all case branches.

        Args:
            index: The current character index being processed.
        """
        if index == n:
            # Base case: reached the end of the string, add current state to results
            results.append("".join(chars))
            return

        if chars[index].isalpha():
            # Branch 1: Keep the current character as lowercase
            chars[index] = chars[index].lower()
            backtrack(index + 1)

            # Branch 2: Switch the current character to uppercase
            chars[index] = chars[index].upper()
            backtrack(index + 1)
        else:
            # If character is a digit, just move to the next index
            backtrack(index + 1)

    backtrack(0)
    return results
