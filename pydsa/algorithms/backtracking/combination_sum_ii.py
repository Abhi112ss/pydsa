METADATA = {
    "id": 40,
    "name": "Combination Sum II",
    "slug": "combination-sum-ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "array", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Find all unique combinations in candidates where the candidate numbers sum to target, each number in candidates may only be used once in the combination.",
}

def solve(candidates: list[int], target: int) -> list[list[int]]:
    """
    Finds all unique combinations in candidates where the numbers sum to target.
    Each number in candidates may only be used once in the combination.

    Args:
        candidates: A list of integers representing the available numbers.
        target: The integer sum we are looking for.

    Returns:
        A list of lists, where each inner list is a unique combination that sums to target.

    Examples:
        >>> solve([10, 1, 2, 7, 6, 1, 5], 8)
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        >>> solve([2, 5, 2, 1, 2], 5)
        [[1, 2, 2], [5]]
    """
    results: list[list[int]] = []
    # Sorting is crucial to handle duplicates and allow early pruning
    candidates.sort()

    def backtrack(remaining_target: int, start_index: int, current_combination: list[int]) -> None:
        if remaining_target == 0:
            # Found a valid combination
            results.append(list(current_combination))
            return

        for i in range(start_index, len(candidates)):
            # If the current number is greater than the remaining target, 
            # no need to check further because the array is sorted.
            if candidates[i] > remaining_target:
                break

            # Skip duplicates: if the current element is the same as the previous 
            # element in the same recursion level, skip it to avoid duplicate combinations.
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue

            # Choose the number
            current_combination.append(candidates[i])
            
            # Move to the next index (i + 1) because each number can be used only once
            backtrack(remaining_target - candidates[i], i + 1, current_combination)
            
            # Backtrack: remove the number to try the next possibility
            current_combination.pop()

    backtrack(target, 0, [])
    return results
