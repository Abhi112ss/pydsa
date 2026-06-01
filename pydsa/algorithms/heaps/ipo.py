METADATA = {
    "id": 502,
    "name": "IPO",
    "slug": "ipo",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "priority_queue", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the number of projects completed given a starting capital and a list of projects with specific capital requirements and profits.",
}

import heapq

def solve(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    """
    Finds the maximum number of projects that can be completed.

    Args:
        k: The maximum number of projects that can be completed.
        w: The initial amount of capital.
        profits: A list of profits for each project.
        capital: A list of capital requirements for each project.

    Returns:
        The maximum number of projects that can be completed.

    Examples:
        >>> solve(2, 0, [1, 2, 3], [0, 1, 1])
        2
        >>> solve(3, 0, [1, 2, 3], [0, 1, 1])
        3
    """
    n = len(profits)
    # Combine profits and capital into a list of tuples and sort by capital requirement.
    # This allows us to efficiently find projects we can afford as our capital grows.
    projects = sorted(zip(capital, profits))
    
    # Max-heap to store profits of projects we can currently afford.
    # Python's heapq is a min-heap, so we store negative profits to simulate a max-heap.
    available_profits_heap = []
    
    project_idx = 0
    completed_projects_count = 0
    current_capital = w

    # We can perform at most k projects.
    for _ in range(k):
        # Add all projects that we can now afford with our current capital into the max-heap.
        while project_idx < n and projects[project_idx][0] <= current_capital:
            # Push negative profit to use heapq as a max-heap.
            heapq.heappush(available_profits_heap, -projects[project_idx][1])
            project_idx += 1
        
        # If there are no affordable projects left in the heap, we cannot proceed further.
        if not available_profits_heap:
            break
        
        # Greedily pick the project with the highest profit.
        current_capital += -heapq.heappop(available_profits_heap)
        completed_projects_count += 1
        
    return completed_projects_count
