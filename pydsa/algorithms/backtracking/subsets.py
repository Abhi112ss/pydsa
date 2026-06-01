METADATA = {
    "id": 78,
    "name": "Subsets",
    "slug": "subsets",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "bit_manipulation", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n * 2^n)",
    "space_complexity": "O(n)",
    "description": "Given an integer array nums of unique elements, return all possible subsets (the power set).",
}

def solve(nums: list[int]) -> list[list[int]]:
    """
    Generates all possible subsets (the power set) of a given list of unique integers.

    Args:
        nums: A list of unique integers.

    Returns:
        A list of lists, where each inner list is a subset of the input.

    Examples:
        >>> solve([1, 2, 3])
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        (Note: Order of subsets may vary)
    """
    result: list[list[int]] = []
    current_subset: list[int] = []

    def backtrack(index: int) -> None:
        # Base case: if we have considered all elements, add the current subset to results
        if index == len(nums):
            result.append(list(current_subset))
            return

        # Decision 1: Include nums[index] in the current subset
        current_subset.append(nums[index])
        backtrack(index + 1)

        # Decision 2: Exclude nums[index] from the current subset (backtrack)
        current_subset.pop()
        backtrack(index + 1)

    backtrack(0)
    return result

def solve_bit_manipulation(nums: list[int]) -> list[list[int]]:
    """
    Alternative implementation using bit manipulation to generate subsets.
    Each bit in an integer from 0 to 2^n - 1 represents whether an element is included.

    Args:
        nums: A list of unique integers.

    Returns:
        A list of lists containing all subsets.
    """
    n = len(nums)
    total_subsets = 1 << n  # 2^n
    result: list[list[int]] = []

    for i in range(total_subsets):
        subset: list[int] = []
        for j in range(n):
            # Check if the j-th bit of i is set
            if (i >> j) & 1:
                subset.append(nums[j])
        result.append(subset)
    
    return result
