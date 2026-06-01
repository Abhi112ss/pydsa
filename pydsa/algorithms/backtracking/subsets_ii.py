METADATA = {
    "id": 90,
    "name": "Subsets II",
    "slug": "subsets-ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "array", "subset"],
    "difficulty": "medium",
    "time_complexity": "O(n * 2^n)",
    "space_complexity": "O(n)",
    "description": "Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.",
}

def solve(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique subsets of an integer array that may contain duplicates.

    Args:
        nums: A list of integers which may contain duplicate elements.

    Returns:
        A list of lists, where each inner list is a unique subset of the input.

    Examples:
        >>> solve([1, 2, 2])
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    """
    # Sort the array to ensure duplicates are adjacent, 
    # which is crucial for the skipping logic.
    nums.sort()
    
    result: list[list[int]] = []
    current_subset: list[int] = []

    def backtrack(start_index: int) -> None:
        # Add a copy of the current subset to the result list
        result.append(list(current_subset))

        for i in range(start_index, len(nums)):
            # If the current element is the same as the previous element 
            # and we are at the same recursion level, skip it to avoid duplicates.
            if i > start_index and nums[i] == nums[i - 1]:
                continue

            # Include the element in the current subset
            current_subset.append(nums[i])
            
            # Move to the next element in the array
            backtrack(i + 1)
            
            # Backtrack: remove the last element to explore other branches
            current_subset.pop()

    backtrack(0)
    return result
