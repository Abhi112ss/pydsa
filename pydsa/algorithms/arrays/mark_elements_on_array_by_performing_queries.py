METADATA = {
    "id": 3080,
    "name": "Mark Elements on Array by Performing Queries",
    "slug": "mark-elements-on-array-by-performing-queries",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "difference_array"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Mark elements in an array within specified ranges using difference array technique for efficient updates.",
}

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Marks elements in the nums array based on range queries.
    
    Each query [left, right] indicates that all elements from index 'left' 
    to 'right' (inclusive) should be marked. The function returns a 
    modified version of nums where marked elements are replaced by 1 
    and unmarked elements remain their original value.

    Args:
        nums: A list of integers representing the initial array.
        queries: A list of lists, where each sub-list contains two integers [left, right].

    Returns:
        A list of integers where elements in the queried ranges are replaced by 1.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [[0, 2], [2, 4]])
        [1, 1, 1, 1, 1]
        >>> solve([10, 20, 30], [[1, 1]])
        [10, 1, 30]
    """
    n = len(nums)
    # difference_array[i] stores the change in the number of marks at index i
    difference_array = [0] * (n + 1)

    # Apply each query to the difference array in O(1)
    for left, right in queries:
        difference_array[left] += 1
        if right + 1 < n:
            difference_array[right + 1] -= 1

    # Compute prefix sums to determine if an index is marked
    current_marks = 0
    result = []
    for i in range(n):
        current_marks += difference_array[i]
        
        # If current_marks > 0, the element at index i was part of at least one query
        if current_marks > 0:
            result.append(1)
        else:
            result.append(nums[i])

    return result
