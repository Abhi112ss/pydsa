METADATA = {
    "id": 2148,
    "name": "Count Elements With Strictly Smaller and Greater Elements",
    "slug": "count-elements-with-strictly-smaller-and-greater-elements",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "hash_map", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count how many elements in an array are strictly smaller and strictly greater than each element.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Calculates the count of elements strictly smaller and strictly greater 
    than each element in the input list.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists where each inner list contains [smaller_count, greater_count] 
        for the corresponding element in the input.

    Examples:
        >>> solve([8, 1, 2, 2, 3])
        [[3, 1], [0, 4], [1, 2], [1, 2], [2, 1]]
        >>> solve([1, 1, 1])
        [[0, 0], [0, 0], [0, 0]]
    """
    n = len(nums)
    if n == 0:
        return []

    # Sort the array to allow binary search for range boundaries
    sorted_nums = sorted(nums)
    
    # Pre-calculate the first and last occurrence of each unique number
    # to determine how many elements are strictly smaller and strictly greater.
    # Using a dictionary to store (smaller_count, greater_count) for each unique value.
    counts_map: dict[int, list[int]] = {}
    
    # We can find the boundaries efficiently by iterating through the sorted array
    # or using binary search. Since we iterate once, we can find boundaries in O(n).
    i = 0
    while i < n:
        current_val = sorted_nums[i]
        
        # Find the first index of current_val (which is 'i')
        # Find the last index of current_val
        start_index = i
        while i < n and sorted_nums[i] == current_val:
            i += 1
        end_index = i - 1
        
        # Elements strictly smaller: all elements before start_index
        smaller_count = start_index
        # Elements strictly greater: all elements after end_index
        greater_count = n - 1 - end_index
        
        counts_map[current_val] = [smaller_count, greater_count]

    # Construct the result based on the original order of nums
    result: list[list[int]] = []
    for num in nums:
        result.append(counts_map[num])
        
    return result
