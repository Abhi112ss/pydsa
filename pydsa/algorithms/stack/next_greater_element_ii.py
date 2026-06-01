METADATA = {
    "id": 503,
    "name": "Next Greater Element II",
    "slug": "next-greater-element-ii",
    "category": "Stack",
    "aliases": [],
    "tags": ["monotonic_stack", "circular_array", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the next greater element for each element in a circular array using a monotonic stack.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds the next greater element for each element in a circular array.

    Args:
        nums: A list of integers representing the circular array.

    Returns:
        A list of integers where each element is the next greater element 
        of the corresponding element in the input list, or -1 if none exists.

    Examples:
        >>> solve([1, 2, 1])
        [2, -1, 2]
        >>> solve([1, 2, 3, 4, 3])
        [2, 3, 4, -1, 4]
    """
    n = len(nums)
    result = [-1] * n
    # The stack stores indices of elements for which we haven't found 
    # the next greater element yet.
    stack: list[int] = []

    # We iterate through the array twice (2 * n) to simulate the circular behavior.
    # The modulo operator allows us to wrap around to the beginning of the array.
    for i in range(2 * n):
        current_index = i % n
        current_value = nums[current_index]

        # While the stack is not empty and the current element is greater than 
        # the element at the index stored at the top of the stack.
        while stack and nums[stack[-1]] < current_value:
            last_index = stack.pop()
            result[last_index] = current_value
        
        # We only push indices to the stack during the first pass to avoid 
        # redundant processing, though pushing in both passes is also correct.
        if i < n:
            stack.append(current_index)

    return result
