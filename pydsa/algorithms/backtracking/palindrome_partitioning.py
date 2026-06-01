METADATA = {
    "id": 131,
    "name": "Palindrome Partitioning",
    "slug": "palindrome_partitioning",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "dynamic_programming", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n * 2^n)",
    "space_complexity": "O(n)",
    "description": "Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.",
}

def solve(s: str) -> list[list[str]]:
    """
    Finds all possible ways to partition a string such that every substring is a palindrome.

    Args:
        s: The input string to be partitioned.

    Returns:
        A list of lists, where each inner list contains a valid palindrome partitioning.

    Examples:
        >>> solve("aab")
        [['a', 'a', 'b'], ['aa', 'b']]
        >>> solve("a")
        [['a']]
    """
    result: list[list[str]] = []
    current_partition: list[str] = []
    n = len(s)

    def is_palindrome(sub_s: str) -> bool:
        """Helper to check if a substring is a palindrome."""
        return sub_s == sub_s[::-1]

    def backtrack(start_index: int) -> None:
        """
        Explores all possible partitions using backtracking.

        Args:
            start_index: The current starting position in the string s.
        """
        # Base case: If we've reached the end of the string, the current partition is valid
        if start_index == n:
            result.append(list(current_partition))
            return

        # Iterate through all possible end positions for the current substring
        for end_index in range(start_index + 1, n + 1):
            substring = s[start_index:end_index]
            
            # If the current substring is a palindrome, proceed to the next part of the string
            if is_palindrome(substring):
                current_partition.append(substring)
                backtrack(end_index)
                # Backtrack: remove the last added substring to explore other possibilities
                current_partition.pop()

    backtrack(0)
    return result
