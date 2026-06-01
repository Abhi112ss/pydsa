METADATA = {
    "id": 46,
    "name": "Permutations",
    "slug": "permutations",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n * n!)",
    "space_complexity": "O(n!)",
    "description": "Given an array nums of distinct integers, return all the possible permutations.",
}

def solve(nums: list[int]) -> list[list[int]]:
    """
    Generates all possible permutations of a list of distinct integers using backtracking.

    Args:
        nums: A list of distinct integers.

    Returns:
        A list of lists, where each inner list is a unique permutation of the input.

    Examples:
        >>> solve([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    results: list[list[int]] = []
    current_permutation: list[int] = []
    used: list[bool] = [False] * len(nums)

    def backtrack() -> None:
        # Base case: if the current permutation is full, add a copy to results
        if len(current_permutation) == len(nums):
            results.append(list(current_permutation))
            return

        for index in range(len(nums)):
            # Skip if the element is already in the current permutation path
            if used[index]:
                continue

            # Choose the element
            used[index] = True
            current_permutation.append(nums[index])

            # Explore further
            backtrack()

            # Backtrack: remove the element and mark as unused for the next branch
            current_permutation.pop()
            used[index] = False

    backtrack()
    return results
