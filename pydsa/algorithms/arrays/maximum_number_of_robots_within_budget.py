METADATA = {
    "id": 2398,
    "name": "Maximum Number of Robots Within Budget",
    "slug": "maximum-number-of-robots-within-budget",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "greedy", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of consecutive robots that can be purchased within a given budget, considering the cost of the most expensive robot in the window.",
}

def solve(costs: list[int], budget: int) -> int:
    """
    Finds the maximum number of consecutive robots that can be purchased 
    within the specified budget. The cost of a window is defined as 
    (max(window) + sum(window)).

    Args:
        costs: A list of integers representing the cost of each robot.
        budget: An integer representing the maximum allowed total cost.

    Returns:
        The maximum number of consecutive robots that fit within the budget.

    Examples:
        >>> solve([3, 5, 1, 3, 6, 7], 20)
        4
        >>> solve([1, 2, 3, 4, 5], 10)
        3
    """
    max_robots = 0
    current_window_sum = 0
    left = 0
    
    # We use a monotonic deque to keep track of the maximum element in the current window
    # in O(1) amortized time.
    from collections import deque
    max_deque = deque()

    for right in range(len(costs)):
        current_window_sum += costs[right]

        # Maintain the deque such that it stores indices of elements in decreasing order
        # The front of the deque will always be the index of the maximum element in the window.
        while max_deque and costs[max_deque[-1]] <= costs[right]:
            max_deque.pop()
        max_deque.append(right)

        # Check if the current window violates the budget constraint:
        # Total cost = sum of elements in window + max element in window
        while max_deque and (current_window_sum + costs[max_deque[0]] > budget):
            current_window_sum -= costs[left]
            # If the element being removed from the window was the maximum, pop it from deque
            if max_deque[0] == left:
                max_deque.popleft()
            left += 1

        # Update the global maximum window size found so far
        max_robots = max(max_robots, right - left + 1)

    return max_robots
