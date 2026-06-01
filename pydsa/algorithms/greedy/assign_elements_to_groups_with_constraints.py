METADATA = {
    "id": 3447,
    "name": "Assign Elements to Groups with Constraints",
    "slug": "assign-elements-to-groups-with-constraints",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Assign elements to groups such that each group satisfies specific constraints using a greedy approach.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Assigns elements to groups such that each group contains elements within a 
    specific range constraint, maximizing the number of groups.

    Args:
        nums: A list of integers representing the elements to be grouped.
        k: The maximum allowed difference between the largest and smallest 
           element in a group (or specific constraint parameter).

    Returns:
        int: The maximum number of groups that can be formed.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 1)
        2
        >>> solve([10, 20, 30], 5)
        1
    """
    if not nums:
        return 0

    # Sort the numbers to allow for a greedy contiguous grouping approach
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    group_count = 0
    i = 0

    while i < n:
        # Start a new group with the current smallest available element
        group_start_val = sorted_nums[i]
        
        # Find the largest index j such that sorted_nums[j] - group_start_val <= k
        # Since the array is sorted, we can greedily consume elements
        current_idx = i
        while current_idx + 1 < n and sorted_nums[current_idx + 1] - group_start_val <= k:
            current_idx += 1
        
        # We have successfully formed one group from index i to current_idx
        group_count += 1
        
        # Move the pointer to the next element after the current group
        i = current_idx + 1

    return group_count
