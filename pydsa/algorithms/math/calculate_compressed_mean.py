METADATA = {
    "id": 2985,
    "name": "Calculate Compressed Mean",
    "slug": "calculate_compressed_mean",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "prefix_sum", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the mean of an array after compressing consecutive identical elements into their counts.",
}

def solve(nums: list[int]) -> float:
    """
    Calculates the mean of the compressed array.
    
    The compression process involves replacing consecutive identical elements 
    with their frequency. For example, [1, 1, 2, 3, 3, 3] becomes [2, 1, 3].
    The mean is the sum of these frequencies divided by the number of unique 
    consecutive groups.

    Args:
        nums: A list of integers representing the original sequence.

    Returns:
        The mean of the compressed sequence as a float.

    Examples:
        >>> solve([1, 1, 2, 3, 3, 3])
        2.0  # Compressed: [2, 1, 3], Mean: (2+1+3)/3 = 2.0
        >>> solve([1, 2, 3])
        1.0  # Compressed: [1, 1, 1], Mean: (1+1+1)/3 = 1.0
    """
    if not nums:
        return 0.0

    total_sum_of_counts = 0
    group_count = 0
    n = len(nums)
    
    i = 0
    while i < n:
        # Start of a new group
        group_count += 1
        current_val = nums[i]
        current_group_size = 0
        
        # Count how many consecutive elements are identical
        while i < n and nums[i] == current_val:
            current_group_size += 1
            i += 1
        
        # The compressed element is the size of the group
        total_sum_of_counts += current_group_size

    # The mean is the sum of the compressed elements (which is just the original length)
    # divided by the number of groups found.
    # Note: The sum of all group sizes is always equal to the length of the original array.
    return float(total_sum_of_counts) / group_count
