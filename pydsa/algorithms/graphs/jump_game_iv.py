METADATA = {
    "id": 1345,
    "name": "Jump Game IV",
    "slug": "jump-game-iv",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "hash_map", "breadth_first_search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of jumps to reach the last index of an array using BFS.",
}

from collections import deque, defaultdict

def solve(arr: list[int]) -> int:
    """
    Finds the minimum number of jumps to reach the last index of the array.

    The problem is modeled as a shortest path problem in an unweighted graph.
    Nodes are indices, and edges exist between:
    1. i -> i + 1
    2. i -> i - 1
    3. i -> all indices j where arr[i] == arr[j]

    Args:
        arr: A list of integers representing the jump possibilities.

    Returns:
        The minimum number of jumps required to reach the last index.

    Examples:
        >>> solve([1, 1, 1, 1])
        3
        >>> solve([12, 1, 1, 1, 12])
        1
        >>> solve([7, 1, 2, 1, 4, 5, 1, 8, 4, 8, 4, 8, 9, 7, 4, 5, 1, 5])
        5
    """
    n = len(arr)
    if n <= 1:
        return 0

    # Map each value to a list of indices where that value occurs
    value_to_indices = defaultdict(list)
    for index, value in enumerate(arr):
        value_to_indices[value].append(index)

    # BFS setup
    queue = deque([(0, 0)])  # (current_index, jump_count)
    visited = {0}

    while queue:
        current_index, jumps = queue.popleft()

        # If we reached the last index, return the jump count
        if current_index == n - 1:
            return jumps

        # Potential next moves: neighbors and same-value indices
        neighbors = []
        
        # 1. Adjacent indices
        if current_index + 1 < n:
            neighbors.append(current_index + 1)
        if current_index - 1 >= 0:
            neighbors.append(current_index - 1)
            
        # 2. Indices with the same value
        # We extract the list once and then clear it to ensure O(n) total complexity
        # Clearing the list prevents re-scanning the same group of indices repeatedly
        same_value_indices = value_to_indices[arr[current_index]]
        for idx in same_value_indices:
            neighbors.append(idx)
        
        # Crucial optimization: once we process all indices of a specific value,
        # we never need to check that value's group again via the hash map.
        del value_to_indices[arr[current_index]]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, jumps + 1))

    return -1
