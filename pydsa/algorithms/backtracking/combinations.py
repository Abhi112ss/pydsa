METADATA = {
    "id": 77,
    "name": "Combinations",
    "slug": "combinations",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "math"],
    "difficulty": "medium",
    "time_complexity": "O(k * C(n, k))",
    "space_complexity": "O(k)",
    "description": "Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].",
}

def solve(n: int, k: int) -> list[list[int]]:
    """
    Finds all possible combinations of k numbers chosen from the range [1, n].

    Args:
        n: The upper bound of the range of numbers (inclusive).
        k: The size of each combination.

    Returns:
        A list of lists, where each inner list is a unique combination of k numbers.

    Examples:
        >>> solve(4, 2)
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        >>> solve(1, 1)
        [[1]]
    """
    result: list[list[int]] = []
    current_combination: list[int] = []

    def backtrack(start_index: int) -> None:
        # Base case: if the combination is of the required size k
        if len(current_combination) == k:
            result.append(list(current_combination))
            return

        # Optimization: Calculate how many more numbers we need to complete the combination
        needed = k - len(current_combination)
        
        # Optimization: Only iterate up to the point where there are enough numbers left to fill k
        # If (n - i + 1) < needed, we cannot possibly complete the combination
        for i in range(start_index, n - needed + 2):
            current_combination.append(i)
            # Move to the next number to ensure combinations are unique and sorted
            backtrack(i + 1)
            # Backtrack: remove the last element to try the next number
            current_combination.pop()

    backtrack(1)
    return result
