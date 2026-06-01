METADATA = {
    "id": 3834,
    "name": "Merge Adjacent Equal Elements",
    "slug": "merge_adjacent_equal_elements",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Iterate through an array and merge adjacent identical elements using a stack-based approach.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Merges adjacent equal elements in the given list using a stack.

    When two adjacent elements are equal, they are merged into a single 
    instance of that element. This process continues if the new merged 
    element matches the element preceding it in the stack.

    Args:
        nums: A list of integers to be processed.

    Returns:
        A list of integers where all adjacent identical elements have been merged.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 3, 4])
        [1, 2, 3, 4]
        >>> solve([1, 1, 1, 1])
        [1]
        >>> solve([1, 2, 3])
        [1, 2, 3]
    """
    if not nums:
        return []

    stack: list[int] = []

    for current_value in nums:
        # If the stack is not empty and the current element matches 
        # the top of the stack, we 'merge' them by simply not adding 
        # the current element (effectively treating them as one).
        if stack and stack[-1] == current_value:
            continue
        else:
            stack.append(current_value)

    return stack
