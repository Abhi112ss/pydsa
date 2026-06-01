METADATA = {
    "id": 2948,
    "name": "Make Lexicographically Smallest Array by Swapping Elements",
    "slug": "make-lexicographically-smallest-array-by-swapping-elements",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy", "union_find"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Rearrange elements to the smallest lexicographical order by swapping elements whose absolute difference is within a given threshold.",
}

def solve(nums: list[int], max_difference: int) -> list[int]:
    """
    Makes the array lexicographically smallest by swapping elements that satisfy 
    the max_difference constraint.

    The core idea is that if |a - b| <= max_difference and |b - c| <= max_difference,
    then a, b, and c can all be swapped with each other (transitive property).
    We group these elements into connected components, sort each component, 
    and place them back into their original indices.

    Args:
        nums: A list of integers.
        max_difference: The maximum allowed difference between two elements to swap.

    Returns:
        A list of integers representing the lexicographically smallest array.

    Examples:
        >>> solve([17, 5, 10, 9, 2], 7)
        [2, 5, 9, 10, 17]
        >>> solve([14, 3, 10, 1, 2], 5)
        [1, 2, 3, 10, 14]
    """
    n = len(nums)
    if n <= 1:
        return nums

    # Create pairs of (value, original_index) and sort them by value
    # This allows us to identify connected components by checking adjacent values
    indexed_nums = sorted([(val, i) for i, val in enumerate(nums)])

    result = [0] * n
    i = 0
    while i < n:
        # Identify a group (component) where each consecutive pair is within max_difference
        group_indices = [indexed_nums[i][1]]
        group_values = [indexed_nums[i][0]]
        
        j = i + 1
        while j < n and indexed_nums[j][0] - indexed_nums[j - 1][0] <= max_difference:
            group_indices.append(indexed_nums[j][1])
            group_values.append(indexed_nums[j][0])
            j += 1
        
        # Sort the original indices to know where the smallest values should go
        # and sort the values to place them in those indices in increasing order
        group_indices.sort()
        group_values.sort()
        
        # Place the sorted values back into the original positions of the group
        for idx, val in zip(group_indices, group_values):
            result[idx] = val
            
        # Move to the start of the next potential group
        i = j

    return result
