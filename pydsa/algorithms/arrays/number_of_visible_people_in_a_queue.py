METADATA = {
    "id": 1944,
    "name": "Number of Visible People in a Queue",
    "slug": "number-of-visible-people-in-a-queue",
    "category": "Stack",
    "aliases": [],
    "tags": ["monotonic_stack", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an array of heights, return an array where each element represents how many people a person can see to their right.",
}

def solve(heights: list[int]) -> list[int]:
    """
    Calculates the number of people each person can see to their right in a queue.
    
    A person can see another person if all people between them are shorter 
    than both the observer and the person being observed.

    Args:
        heights: A list of integers representing the heights of people in a queue.

    Returns:
        A list of integers where the i-th integer is the number of people 
        the i-th person can see to their right.

    Examples:
        >>> solve([10, 6, 8, 5, 11, 9])
        [3, 1, 2, 1, 1, 0]
        >>> solve([1, 3, 2, 4, 5])
        [1, 2, 1, 1, 0]
    """
    n = len(heights)
    result = [0] * n
    # The stack will store heights of people to the right in a monotonic decreasing order.
    # However, we process from right to left to easily determine visibility for the current person.
    stack: list[int] = []

    # Iterate backwards through the queue
    for i in range(n - 1, -1, -1):
        current_height = heights[i]
        visible_count = 0
        
        # A person can see everyone in the stack who is shorter than them,
        # because those shorter people act as 'blockers' for anyone further right.
        # Once we encounter someone taller or equal, they block the view of anyone further right.
        while stack and current_height > stack[-1]:
            stack.pop()
            visible_count += 1
            
        # If the stack is not empty after popping shorter people, 
        # the current person can also see the next person who is taller than them.
        if stack:
            visible_count += 1
            
        result[i] = visible_count
        
        # Maintain the monotonic decreasing property for the next person to the left
        stack.append(current_height)
        
    return result
