METADATA = {
    "id": 752,
    "name": "Open the Lock",
    "slug": "open-the-lock",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "shortest_path", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(10^4)",
    "space_complexity": "O(10^4)",
    "description": "Find the minimum number of turns to reach a target combination from '0000' without hitting any deadends.",
}

from collections import deque

def solve(deadends: list[str], target: str) -> int:
    """
    Finds the minimum number of turns to reach the target combination using BFS.

    Args:
        deadends: A list of forbidden combinations.
        target: The target combination to reach.

    Returns:
        The minimum number of turns required, or -1 if the target is unreachable.

    Examples:
        >>> solve(["0201", "0101", "0102", "1212", "2002"], "0202")
        6
        >>> solve(["8888"], "8888")
        0
        >>> solve(["0000"], "8888")
        -1
    """
    dead_set = set(deadends)
    start_node = "0000"

    # Edge case: if the starting position is a deadend, we can't move.
    if start_node in dead_set:
        return -1
    
    # Edge case: if we are already at the target.
    if start_node == target:
        return 0

    # BFS queue stores tuples of (current_combination, current_depth)
    queue = deque([(start_node, 0)])
    visited = {start_node}

    while queue:
        current_combination, depth = queue.popleft()

        # Generate all 8 possible next moves (4 wheels, 2 directions each)
        for i in range(4):
            digit = int(current_combination[i])
            
            # Try both directions: +1 and -1 (modulo 10)
            for direction in [-1, 1]:
                new_digit = (digit + direction) % 10
                # Construct the new combination string
                new_combination = (
                    current_combination[:i] + 
                    str(new_digit) + 
                    current_combination[i+1:]
                )

                if new_combination == target:
                    return depth + 1

                # If not a deadend and not visited, add to queue
                if new_combination not in dead_set and new_combination not in visited:
                    visited.add(new_combination)
                    queue.append((new_combination, depth + 1))

    return -1
