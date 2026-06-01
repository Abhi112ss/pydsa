METADATA = {
    "id": 3211,
    "name": "Generate Binary Strings Without Adjacent Zeros",
    "slug": "generate-binary-strings-without-adjacent-zeros",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "string"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Generate all binary strings of length n such that no two zeros are adjacent.",
}

def solve(n: int) -> list[str]:
    """
    Generates all binary strings of length n where no two zeros are adjacent.

    Args:
        n: The length of the binary strings to generate.

    Returns:
        A list of strings representing all valid binary sequences.

    Examples:
        >>> solve(3)
        ['010', '011', '101', '110', '111']
    """
    if n <= 0:
        return []
    
    result: list[str] = []

    def backtrack(current_string: list[str]) -> None:
        """
        Recursive helper to build the string character by character.

        Args:
            current_string: The list of characters representing the string built so far.
        """
        # Base case: if the string reaches the target length, add it to results
        if len(current_string) == n:
            result.append("".join(current_string))
            return

        # Option 1: Always allowed to append '1'
        current_string.append("1")
        backtrack(current_string)
        current_string.pop()

        # Option 2: Append '0' only if it's the first char or the previous char was '1'
        # This prevents adjacent zeros.
        if not current_string or current_string[-1] == "1":
            current_string.append("0")
            backtrack(current_string)
            current_string.pop()

    # Start the recursion with an empty list
    backtrack([])
    
    # The problem usually expects lexicographical order or specific order.
    # Sorting ensures consistency if the backtracking order varies.
    return sorted(result)
