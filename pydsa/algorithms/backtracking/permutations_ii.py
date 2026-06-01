METADATA = {
    "id": 47,
    "name": "Permutations II",
    "slug": "permutations-ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n * n!)",
    "space_complexity": "O(n!)",
    "description": "Given a collection of numbers, possibly containing duplicates, return all possible unique permutations in any order.",
}

def solve(nums: list[int]) -> list[list[int]]:
    """
    Generates all unique permutations of a list of integers that may contain duplicates.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists, where each inner list is a unique permutation.

    Examples:
        >>> solve([1, 1, 2])
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> solve([1, 2])
        [[1, 2], [2, 1]]
    """
    results: list[list[int]] = []
    # Sorting is crucial to ensure duplicates are adjacent, 
    # allowing us to skip them easily during backtracking.
    nums.sort()
    used: list[bool] = [False] * len(nums)

    def backtrack(current_permutation: list[int]) -> None:
        if len(current_permutation) == len(nums):
            results.append(list(current_permutation))
            return

        for i in range(len(nums)):
            # Skip if this specific index has already been used in the current path
            if used[i]:
                continue

            # Skip duplicate elements:
            # If the current element is the same as the previous one AND
            # the previous one was not used in this path, it means we already 
            # processed this value at this recursion level.
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            # Standard backtracking pattern: Choose, Explore, Un-choose
            used[i] = True
            current_permutation.append(nums[i])
            
            backtrack(current_permutation)
            
            current_permutation.pop()
            used[i] = False

    backtrack([])
    return results
