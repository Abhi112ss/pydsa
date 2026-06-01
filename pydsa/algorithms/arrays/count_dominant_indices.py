METADATA = {
    "id": 3833,
    "name": "Count Dominant Indices",
    "slug": "count_dominant_indices",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "prefix_sum", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count indices where the element is strictly greater than the average of all elements to its left.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of indices i such that nums[i] is strictly greater 
    than the average of all elements in the prefix nums[0...i-1].

    Args:
        nums: A list of integers.

    Returns:
        The count of dominant indices.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        4
        >>> solve([10, 1, 1, 1])
        1
        >>> solve([1, 1, 1, 1])
        0
    """
    if not nums:
        return 0

    dominant_count = 0
    running_sum = 0

    for i in range(len(nums)):
        # For the first element, there are no elements to its left.
        # The problem definition usually implies the average of an empty set 
        # is treated such that the first element cannot be dominant, 
        # or we only start checking from index 1.
        if i > 0:
            # Calculate average of elements from index 0 to i-1
            # Using floating point division to ensure precision
            average_left = running_sum / i
            
            if nums[i] > average_left:
                dominant_count += 1
        
        # Update the running sum to include the current element for the next iteration
        running_sum += nums[i]

    return dominant_count
