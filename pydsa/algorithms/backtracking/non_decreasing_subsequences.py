METADATA = {
    "id": 491,
    "name": "Non-decreasing Subsequences",
    "slug": "non-decreasing-subsequences",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "hash_set", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(2^n * n)",
    "space_complexity": "O(2^n)",
    "description": "Find all non-decreasing subsequences of an array that have at least two elements.",
}

def solve(nums: list[int]) -> list[list[int]]:
    """
    Finds all non-decreasing subsequences of the given array with at least two elements.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists, where each inner list is a non-decreasing subsequence.

    Examples:
        >>> solve([4, 6, 7, 7])
        [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
        >>> solve([4, 4, 4])
        [[4, 4], [4, 4, 4], [4, 4]] # Note: The logic handles duplicates via set per level
    """
    results: list[list[int]] = []
    n = len(nums)

    def backtrack(start_index: int, current_subsequence: list[int]) -> None:
        # If the current subsequence has at least 2 elements, it's a valid result
        if len(current_subsequence) >= 2:
            results.append(list(current_subsequence))

        # Use a set to track elements used at the CURRENT recursion level
        # This prevents duplicate subsequences when the input has duplicate numbers
        used_in_this_level = set()

        for i in range(start_index, n):
            # Skip if we have already used this number at this specific depth
            if nums[i] in used_in_this_level:
                continue
            
            # Check if the current number maintains the non-decreasing property
            if not current_subsequence or nums[i] >= current_subsequence[-1]:
                used_in_this_level.add(nums[i])
                
                # Choose the element
                current_subsequence.append(nums[i])
                
                # Explore further
                backtrack(i + 1, current_subsequence)
                
                # Backtrack (remove the element)
                current_subsequence.pop()

    backtrack(0, [])
    return results
