METADATA = {
    "id": 768,
    "name": "Max Chunks To Make Sorted II",
    "slug": "max-chunks-to-make-sorted-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of chunks such that sorting each chunk and concatenating them results in a sorted array.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the maximum number of chunks the array can be split into such that
    sorting each chunk individually and concatenating them results in a sorted array.

    The algorithm uses a monotonic stack approach. The stack stores the maximum 
    value of each chunk found so far. When a new element is encountered that is 
    smaller than the maximum of the previous chunk, it means the current element 
    must belong to the same chunk as the previous maximums. We merge these chunks 
    by popping from the stack until the stack's top is less than or equal to 
    the current element.

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
    # The stack will store the maximum value of each chunk.
    # Each element in the stack represents a distinct chunk.
    max_stack: list[int] = []

    for current_val in arr:
        # If the stack is empty or the current value is greater than or equal 
        # to the max of the last chunk, this value can potentially start a new chunk.
        if not max_stack or current_val >= max_stack[-1]:
            max_stack.append(current_val)
        else:
            # If current_val is smaller than the max of the last chunk, 
            # it must be part of that chunk (and potentially previous chunks).
            # We record the current maximum to restore it after merging.
            current_chunk_max = max_stack.pop()
            
            # Merge all chunks whose maximum value is greater than the current value.
            # This effectively combines multiple chunks into one larger chunk.
            while max_stack and max_stack[-1] > current_val:
                max_stack.pop()
            
            # Push the maximum value of the newly merged chunk back onto the stack.
            max_stack.append(current_chunk_max)

    return len(max_stack)
