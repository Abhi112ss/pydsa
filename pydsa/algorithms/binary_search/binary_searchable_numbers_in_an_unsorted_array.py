METADATA = {
    "id": 1966,
    "name": "Binary Searchable Numbers in an Unsorted Array",
    "slug": "binary-searchable-numbers-in-an-unsorted-array",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "binary_search", "prefix_max", "suffix_min"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find all numbers in an array that can be used as a pivot for binary search, meaning they are greater than or equal to all elements to their left and less than or equal to all elements to their right.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds all numbers in the array that satisfy the binary search property.
    
    A number at index i is searchable if:
    max(nums[0...i-1]) <= nums[i] <= min(nums[i+1...n-1])

    Args:
        nums: A list of integers.

    Returns:
        A list of integers that are searchable, sorted in ascending order.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
        >>> solve([5, 4, 3, 2, 1])
        [1]
        >>> solve([1, 3, 2, 4, 5])
        [1, 4, 5]
    """
    n = len(nums)
    if n == 0:
        return []

    # left_max[i] will store the maximum value from index 0 to i
    left_max = [0] * n
    current_max = float('-inf')
    for i in range(n):
        if nums[i] > current_max:
            current_max = nums[i]
        left_max[i] = current_max

    # right_min[i] will store the minimum value from index i to n-1
    right_min = [0] * n
    current_min = float('inf')
    for i in range(n - 1, -1, -1):
        if nums[i] < current_min:
            current_min = nums[i]
        right_min[i] = current_min

    searchable_elements = []
    
    # A number is searchable if it is >= max of elements to its left
    # AND <= min of elements to its right.
    # Note: For index 0, left_max is just nums[0].
    # For index n-1, right_min is just nums[n-1].
    for i in range(n):
        # Check if current element is >= max of everything to its left
        # and <= min of everything to its right.
        # Since left_max[i] includes nums[i], we check left_max[i] == nums[i]
        # and right_min[i] == nums[i].
        if nums[i] == left_max[i] and nums[i] == right_min[i]:
            searchable_elements.append(nums[i])

    # The problem asks for the result in ascending order.
    # Since we collected them in original order, we sort them.
    searchable_elements.sort()
    return searchable_elements
