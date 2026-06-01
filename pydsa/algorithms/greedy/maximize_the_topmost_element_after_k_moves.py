METADATA = {
    "id": 2202,
    "name": "Maximize the Topmost Element After K Moves",
    "slug": "maximize-the-topmost-element-after-k-moves",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "stack", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(k)",
    "space_complexity": "O(1)",
    "description": "Maximize the value of the topmost element of a stack after performing at most k removal operations.",
}

def solve(moves: int, elements: list[int]) -> int:
    """
    Finds the maximum possible value of the topmost element after at most k moves.
    
    The strategy is to greedily remove elements from the top of the stack to 
    expose the largest possible value. Since we can choose to stop at any 
    point between 0 and k moves, we track the maximum value seen so far.

    Args:
        moves: The maximum number of elements that can be removed from the top.
        elements: A list of integers representing the stack from top to bottom.

    Returns:
        The maximum value that can be at the top of the stack.

    Examples:
        >>> solve(2, [1, 2, 3, 4, 5])
        5
        >>> solve(3, [1, 2, 3, 4, 5])
        5
        >>> solve(1, [1, 2, 3, 4, 5])
        2
    """
    # The current maximum is the element at the very top (0 moves)
    max_top_value = elements[0]
    
    # We can perform between 1 and 'moves' removals.
    # If we remove 'i' elements, the new top is elements[i].
    # However, if we remove all elements up to the last one, 
    # the new top is the element that was at index 'i'.
    # We iterate through the possible number of removals.
    for i in range(1, moves + 1):
        # If we have removed i elements, the new top is elements[i]
        # We must ensure we don't go out of bounds of the list.
        # If i == len(elements), it means we've removed everything, 
        # but the problem implies we want the topmost element *after* moves.
        # If we remove all elements, the stack becomes empty (not possible per constraints).
        # The constraint usually implies we look at the element at index i.
        if i < len(elements):
            current_top = elements[i]
            if current_top > max_top_value:
                max_top_value = current_top
        else:
            # If we've exhausted the list, we can't expose more elements.
            break
            
    return max_top_value
