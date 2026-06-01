METADATA = {
    "id": 320,
    "name": "Generalized Abbreviation",
    "slug": "generalized-abbreviation",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "bit_manipulation", "string"],
    "difficulty": "hard",
    "time_complexity": "O(2^n * n)",
    "space_complexity": "O(n)",
    "description": "Given a string, return all possible generalized abbreviations by replacing non-overlapping substrings with their lengths.",
}

def solve(word: str) -> list[str]:
    """
    Generates all possible generalized abbreviations of a given word.

    Args:
        word: The input string to abbreviate.

    Returns:
        A list of all possible abbreviated strings.

    Examples:
        >>> solve("word")
        ['4', 'w3', 'wo2', 'wor1', 'word', 'w1rd', 'wo1d', 'wor1d', ...] (all 16 combinations)
    """
    results: list[str] = []
    n = len(word)

    def backtrack(index: int, current_path: list[str], count: int) -> None:
        """
        Recursive helper to explore all abbreviation possibilities.

        Args:
            index: Current character index being processed.
            current_path: List of strings representing the current abbreviation state.
            count: Number of consecutive characters currently being abbreviated into a number.
        """
        if index == n:
            # Base case: reached end of word. If there's a pending count, append it.
            final_str = "".join(current_path)
            if count > 0:
                final_str += str(count)
            results.append(final_str)
            return

        # Option 1: Abbreviate the current character (increment the count)
        # We don't add to current_path yet, just increase the number of characters to skip
        backtrack(index + 1, current_path, count + 1)

        # Option 2: Keep the current character as is
        # If we were counting characters to abbreviate, we must "flush" that count first
        new_path = current_path[:]
        if count > 0:
            new_path.append(str(count))
        new_path.append(word[index])
        backtrack(index + 1, new_path, 0)

    backtrack(0, [], 0)
    return results
