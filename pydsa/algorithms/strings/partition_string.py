METADATA = {
    "id": 3597,
    "name": "Partition String",
    "slug": "partition_string",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["strings", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Partition a string into all possible non-empty substrings.",
}

def solve(s: str) -> list[list[str]]:
    """
    Partitions a string into all possible non-empty substrings using backtracking.

    Args:
        s: The input string to be partitioned.

    Returns:
        A list of lists, where each inner list represents a valid partition 
        of the input string.

    Examples:
        >>> solve("abc")
        [['a', 'b', 'c'], ['a', 'bc'], ['ab', 'c']]
    """
    result: list[list[str]] = []
    current_partition: list[str] = []
    n = len(s)

    def backtrack(start_index: int) -> None:
        # If we have reached the end of the string, add the current partition to results
        if start_index == n:
            result.append(list(current_partition))
            return

        # Explore all possible end positions for the next substring
        for end_index in range(start_index + 1, n + 1):
            # Extract the substring from start_index to end_index
            substring = s[start_index:end_index]
            current_partition.append(substring)
            
            # Recurse to partition the remaining part of the string
            backtrack(end_index)
            
            # Backtrack: remove the last added substring to try the next split point
            current_partition.pop()

    backtrack(0)
    return result
