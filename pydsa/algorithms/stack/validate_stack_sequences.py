METADATA = {
    "id": 946,
    "name": "Validate Stack Sequences",
    "slug": "validate-stack-sequences",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "simulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a sequence of push and pop operations could have resulted in a given target sequence.",
}

def solve(pushed: list[int], popped: list[int]) -> bool:
    """
    Validates if the given popped sequence can be produced by the pushed sequence
    using a stack.

    Args:
        pushed: A list of integers representing the order of elements pushed onto the stack.
        popped: A list of integers representing the order of elements popped from the stack.

    Returns:
        True if the popped sequence is valid, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
        True
        >>> solve([1, 2, 3, 4, 5], [4, 3, 5, 1])
        False
    """
    stack: list[int] = []
    popped_index = 0
    n = len(pushed)

    for value in pushed:
        # Simulate the push operation
        stack.append(value)
        
        # Greedily pop elements from the stack as long as the top of the stack
        # matches the current element we are looking for in the popped sequence.
        while stack and popped_index < n and stack[-1] == popped[popped_index]:
            stack.pop()
            popped_index += 1

    # If the stack is empty, it means all elements were pushed and popped 
    # in a valid sequence matching the target.
    return not stack
