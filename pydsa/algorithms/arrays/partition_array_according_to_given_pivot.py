METADATA = {
    "id": 2161,
    "name": "Partition Array According to Given Pivot",
    "slug": "partition_array_according_to_given_pivot",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "partition"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Partition an array into three parts: elements less than pivot, elements equal to pivot, and elements greater than pivot, preserving relative order.",
}

def solve(nums: list[int], pivot: int) -> list[int]:
    """
    Partitions the array into three segments based on a pivot value.
    
    The segments are:
    1. Elements strictly less than the pivot.
    2. Elements equal to the pivot.
    3. Elements strictly greater than the pivot.
    Relative order of elements within each segment is preserved.

    Args:
        nums: A list of integers to be partitioned.
        pivot: The integer value used as the pivot.

    Returns:
        A new list containing the partitioned elements.

    Examples:
        >>> solve([9, 12, 5, 10, 14, 10, 10, 8, 11], 10)
        [9, 5, 8, 10, 10, 10, 12, 14, 11]
        >>> solve([2, 2, 2, 2, 2], 2)
        [2, 2, 2, 2, 2]
    """
    # Initialize three separate lists to hold the partitioned elements
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    # Single pass through the array to categorize each element
    for num in nums:
        if num < pivot:
            less_than_pivot.append(num)
        elif num == pivot:
            equal_to_pivot.append(num)
        else:
            greater_than_pivot.append(num)

    # Concatenate the lists in the required order: less, equal, then greater
    return less_than_pivot + equal_to_pivot + greater_than_pivot
