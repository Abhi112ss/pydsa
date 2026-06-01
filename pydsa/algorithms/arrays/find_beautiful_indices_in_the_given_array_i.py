METADATA = {
    "id": 3006,
    "name": "Find Beautiful Indices in the Given Array I",
    "slug": "find-beautiful-indices-in-the-given-array-i",
    "category": "Array",
    "aliases": [],
    "tags": ["string_matching", "array", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Find all indices i such that pattern1 exists at i and pattern2 exists at some index j where |i - j| <= max_diff.",
}

def solve(nums: list[int], pattern1: list[int], pattern2: list[int], max_diff: int) -> list[int]:
    """
    Finds all indices 'i' where pattern1 starts at 'i' and pattern2 starts at some 'j'
    such that the absolute difference between 'i' and 'j' is at most 'max_diff'.

    Args:
        nums: The input integer array.
        pattern1: The first pattern to search for.
        pattern2: The second pattern to search for.
        max_diff: The maximum allowed absolute difference between indices.

    Returns:
        A sorted list of indices 'i' that satisfy the condition.

    Examples:
        >>> solve([1, 2, 1, 2, 1], [1, 2], [2, 1], 1)
        [0, 2]
    """
    n = len(nums)
    m1 = len(pattern1)
    m2 = len(pattern2)
    
    # Find all starting indices for pattern1
    indices1 = []
    for i in range(n - m1 + 1):
        # Check if pattern1 matches starting at i
        match = True
        for k in range(m1):
            if nums[i + k] != pattern1[k]:
                match = False
                break
        if match:
            indices1.append(i)
            
    # Find all starting indices for pattern2
    indices2 = []
    for j in range(n - m2 + 1):
        # Check if pattern2 matches starting at j
        match = True
        for k in range(m2):
            if nums[j + k] != pattern2[k]:
                match = False
                break
        if match:
            indices2.append(j)
            
    if not indices1 or not indices2:
        return []

    beautiful_indices = []
    p2_idx = 0
    
    # For each index in indices1, find if there is a valid index in indices2
    # using a two-pointer approach since both lists are naturally sorted
    for i in indices1:
        # Move the pointer in indices2 to the first possible candidate
        # that could satisfy the condition |i - j| <= max_diff
        while p2_idx < len(indices2) and indices2[p2_idx] < i - max_diff:
            p2_idx += 1
            
        # Check if the current candidate in indices2 satisfies the upper bound
        if p2_idx < len(indices2) and abs(indices2[p2_idx] - i) <= max_diff:
            beautiful_indices.append(i)
            
    return beautiful_indices
