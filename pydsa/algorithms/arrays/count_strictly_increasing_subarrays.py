METADATA = {
    "id": 2393,
    "name": "Count Strictly Increasing Subarrays",
    "slug": "count-strictly-increasing-subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "arrays", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of strictly increasing subarrays in a given integer array.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of strictly increasing subarrays in the input list.

    A subarray is strictly increasing if each element is strictly greater 
    than the previous one. The algorithm identifies maximal contiguous 
    increasing segments and uses the arithmetic series formula to count 
    all possible subarrays within those segments.

    Args:
        nums: A list of integers.

    Returns:
        The total count of strictly increasing subarrays.

    Examples:
        >>> solve([1, 2, 3, 4])
        10
        >>> solve([1, 3, 2, 4])
        5
        >>> solve([1, 1, 1])
        3
    """
    if not nums:
        return 0

    total_count = 0
    current_segment_length = 1

    for i in range(1, len(nums)):
        # Check if the current element continues the strictly increasing sequence
        if nums[i] > nums[i - 1]:
            current_segment_length += 1
        else:
            # If the sequence breaks, calculate subarrays for the completed segment
            # A segment of length L has L*(L+1)/2 subarrays, but we subtract 
            # the single-element subarrays later or handle them via the formula.
            # To avoid double counting and simplify, we use the property that 
            # adding an element to a segment of length L adds L new subarrays.
            # However, the most robust way is to sum up the 'new' subarrays 
            # formed at each step.
            current_segment_length = 1

        # Instead of calculating at the end of a segment, we add the number 
        # of new strictly increasing subarrays ending at index i.
        # If the segment length is L, there are L subarrays ending at i.
        # Example: [1, 2, 3] -> at index 0: [1] (len 1), at index 1: [2], [1,2] (len 2), 
        # at index 2: [3], [2,3], [1,2,3] (len 3). Total = 1+2+3 = 6.
        total_count += current_segment_length

    # The loop starts from index 1, so we must account for the first element
    # which always forms a subarray of length 1.
    # Actually, the logic above handles it if we initialize total_count correctly.
    # Let's refine:
    
    # Re-calculating with a cleaner approach:
    total_count = 0
    length = 0
    for i in range(len(nums)):
        if i > 0 and nums[i] > nums[i-1]:
            length += 1
        else:
            length = 1
        total_count += length
        
    return total_count
