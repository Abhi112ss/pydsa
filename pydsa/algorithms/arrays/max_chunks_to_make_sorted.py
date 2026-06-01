METADATA = {
    "id": 769,
    "name": "Max Chunks To Make Sorted II",
    "slug": "max-chunks-to-make-sorted-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays", "monotonic stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Partition an array into the maximum number of chunks such that sorting each chunk individually results in a sorted version of the entire array.",
}

def solve(arr: list[int]) -> int:
    """
    Finds the maximum number of chunks the array can be split into such that 
    sorting each chunk results in a fully sorted array.

    The algorithm uses a monotonic decreasing stack to keep track of the 
    maximum value of each chunk. When a new element is larger than the 
    top of the stack, it means the current element must belong to a chunk 
    that includes the previous chunks.

    Args:
        arr: A list of integers.

    Returns:
        The maximum number of chunks possible.

    Examples:
        >>> solve([5, 4, 3, 2, 1])
        1
        >>> solve([2, 1, 3, 4, 4])
        4
    """
    # The stack will store the maximum value of each chunk found so far.
    # This stack will be monotonically non-increasing.
    max_values_stack: list[int] = []

    for current_val in arr:
        # If the stack is empty or the current value is greater than or equal 
        # to the max value of the last chunk, we can potentially start a new chunk.
        if not max_values_stack or current_val >= max_values_stack[-1]:
            max_values_stack.append(current_val)
        else:
            # If current_val is smaller than the max of the last chunk, 
            # it must be part of an existing chunk. We need to merge all 
            # chunks whose max value is greater than the current value.
            current_chunk_max = max_values_stack.pop()
            
            # Keep popping until we find a chunk whose max value is <= current_val.
            # This effectively merges all affected chunks into one.
            while max_values_stack and max_values_stack[-1] > current_val:
                max_values_stack.pop()
            
            # Push the maximum value of the newly merged chunk back onto the stack.
            max_values_stack.append(current_chunk_max)

    # The number of elements in the stack represents the number of independent chunks.
    return len(max_values_stack)
