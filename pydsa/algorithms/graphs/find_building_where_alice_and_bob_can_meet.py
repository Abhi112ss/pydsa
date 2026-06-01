METADATA = {
    "id": 2940,
    "name": "Find Building Where Alice and Bob Can Meet",
    "slug": "find-building-where-alice-and-bob-can-meet",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the smallest index of a building that both Alice and Bob can reach, considering that they cannot pass through buildings with a height difference greater than 1.",
}

def solve(n: int, height: list[int], alice_start: int, bob_start: int) -> int:
    """
    Args:
        n: The number of buildings.
        height: A list of integers representing the height of each building.
        alice_start: The starting building index for Alice.
        bob_start: The starting building index for Bob.

    Returns:
        The smallest index of a building reachable by both, or -1 if none exists.
    """
    def get_reachable_set(start_node: int) -> set[int]:
        reachable = {start_node}
        stack = [start_node]
        while stack:
            current = stack.pop()
            for neighbor in [current - 1, current + 1]:
                if 0 <= neighbor < n and neighbor not in reachable:
                    if abs(height[current] - height[neighbor]) <= 1:
                        reachable.add(neighbor)
                        stack.append(neighbor)
        return reachable

    alice_reachable = get_reachable_set(alice_start)
    bob_reachable = get_reachable_set(bob_start)
    
    intersection = alice_reachable.intersection(bob_reachable)
    
    if not intersection:
        return -1
    
    return min(intersection)