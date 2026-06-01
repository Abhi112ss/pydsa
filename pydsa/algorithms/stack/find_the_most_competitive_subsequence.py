METADATA = {
    "id": 1673,
    "name": "Find the Most Competitive Subsequence",
    "slug": "find-the-most-competitive-subsequence",
    "category": "Stack",
    "aliases": [],
    "tags": ["monotonic_stack", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find a subsequence of length k that is lexicographically smallest.",
}

def solve(candidates: list[int], k: int) -> list[int]:
    """
    Finds the lexicographically smallest subsequence of length k.

    Args:
        candidates: A list of integers to choose from.
        k: The required length of the subsequence.

    Returns:
        A list of integers representing the most competitive subsequence.

    Examples:
        >>> solve([3, 5, 2, 6], 2)
        [2, 6]
        >>> solve([2, 4, 3, 3, 5, 4, 9, 6], 4)
        [2, 3, 3, 4]
    """
    stack: list[int] = []
    # total_rem_to_discard is the number of elements we are allowed to skip
    # to maintain a subsequence of length k.
    total_rem_to_discard = len(candidates) - k

    for num in candidates:
        # While the stack is not empty, the current number is smaller than the top,
        # and we still have 'discard credits' left, pop from the stack to maintain
        # a monotonic increasing property (lexicographical smallest).
        while stack and stack[-1] > num and total_rem_to_discard > 0:
            stack.pop()
            total_rem_to_discard -= 1
        
        stack.append(num)

    # If we haven't discarded enough elements (e.g., the input was already sorted),
    # we truncate the stack to the required length k.
    return stack[:k]
