METADATA = {
    "id": 1285,
    "name": "Find the Start and End Number of Continuous Ranges",
    "slug": "find-the-start-and-end-number-of-continuous-ranges",
    "category": "Array",
    "aliases": [],
    "tags": ["math", "group_by", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Identify the start and end numbers of all continuous ranges in a given list of integers.",
}

def solve(nums: list[int]) -> list[list[int]]:
    """
    Finds the start and end numbers of all continuous ranges in the input list.

    A continuous range is a sequence of numbers where each subsequent number 
    is exactly one greater than the previous one when sorted.

    Args:
        nums: A list of integers.

    Returns:
        A list of lists, where each inner list contains exactly two integers 
        representing the [start, end] of a continuous range.

    Examples:
        >>> solve([1, 2, 3, 5, 6, 8, 10, 11, 12])
        [[1, 3], [5, 6], [8, 8], [10, 12]]
        >>> solve([1, 5, 2, 4, 3])
        [[1, 5]]
    """
    if not nums:
        return []

    # Sort the numbers to process them in ascending order
    # Time complexity: O(n log n)
    sorted_nums = sorted(nums)
    
    ranges = []
    if not sorted_nums:
        return ranges

    # Initialize the first range with the first element
    range_start = sorted_nums[0]
    current_prev = sorted_nums[0]

    for i in range(1, len(sorted_nums)):
        current_val = sorted_nums[i]
        
        # Check if the current number continues the existing sequence
        if current_val == current_prev + 1:
            current_prev = current_val
        else:
            # The sequence broke, so close the current range and start a new one
            ranges.append([range_start, current_prev])
            range_start = current_val
            current_prev = current_val

    # Append the final range after the loop finishes
    ranges.append([range_start, current_prev])

    return ranges
