METADATA = {
    "id": 39,
    "name": "Combination Sum",
    "slug": "combination-sum",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(N^(T/M + 1)) where N is len(candidates), T is target, M is min(candidates)",
    "space_complexity": "O(T/M)",
    "description": "Find all unique combinations in candidates where the chosen numbers sum to target, allowing the same number to be chosen an unlimited number of times.",
}

def solve(candidates: list[int], target: int) -> list[list[int]]:
    """
    Finds all unique combinations in candidates that sum up to the target.

    Args:
        candidates: A list of integers representing the available numbers.
        target: The integer sum we want to achieve.

    Returns:
        A list of lists, where each inner list is a unique combination of 
        candidates that sums to the target.

    Examples:
        >>> solve([2, 3, 6, 7], 7)
        [[2, 2, 3], [7]]
        >>> solve([2, 3, 5], 8)
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    """
    results: list[list[int]] = []
    # Sorting helps in pruning the search tree early
    candidates.sort()

    def backtrack(remaining: int, start_index: int, current_combination: list[int]) -> None:
        """
        Recursive helper function to explore combinations using backtracking.

        Args:
            remaining: The remaining value needed to reach the target.
            start_index: The index in candidates to start searching from to avoid duplicates.
            current_combination: The list of numbers chosen in the current path.
        """
        # Base case: target reached
        if remaining == 0:
            results.append(list(current_combination))
            return

        for i in range(start_index, len(candidates)):
            candidate = candidates[i]

            # Optimization: Since candidates are sorted, if the current candidate 
            # exceeds the remaining target, no subsequent candidates will work.
            if candidate > remaining:
                break

            # Choose the number
            current_combination.append(candidate)

            # Explore: We pass 'i' as the next start_index instead of 'i + 1' 
            # because the same number can be reused multiple times.
            backtrack(remaining - candidate, i, current_combination)

            # Backtrack: Remove the last number to try the next candidate
            current_combination.pop()

    backtrack(target, 0, [])
    return results
