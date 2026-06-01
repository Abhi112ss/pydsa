METADATA = {
    "id": 962,
    "name": "Maximum Width Ramp",
    "slug": "maximum-width-ramp",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum width of a ramp defined by indices i and j such that i < j and arr[i] <= arr[j].",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the maximum width of a ramp in the given array.
    
    A ramp is defined as a pair of indices (i, j) such that i < j and arr[i] <= arr[j].
    The width of the ramp is j - i.

    Args:
        arr: A list of integers.

    Returns:
        The maximum width of a ramp in the array. Returns 0 if no ramp exists.

    Examples:
        >>> solve([6, 0, 8, 2, 1, 5])
        4
        >>> solve([9, 8, 1, 0, 1, 9, 4, 0, 4, 1])
        7
    """
    n = len(arr)
    stack = []

    # Step 1: Build a monotonic decreasing stack of indices.
    # We only care about indices that could potentially be the start of a ramp.
    # If arr[i] > arr[some_previous_index], then i will never be a better 
    # starting index than some_previous_index because the previous index 
    # is smaller and further to the left.
    for i in range(n):
        if not stack or arr[stack[-1]] > arr[i]:
            stack.append(i)

    max_width = 0

    # Step 2: Iterate backwards from the end of the array.
    # For each j, we check if it can form a ramp with the indices in our stack.
    # Since we want to maximize j - i, and we are iterating j from right to left,
    # we can pop indices from the stack once they satisfy the condition.
    for j in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[j]:
            start_index = stack.pop()
            max_width = max(max_width, j - start_index)

    return max_width
