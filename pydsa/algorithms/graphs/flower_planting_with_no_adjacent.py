METADATA = {
    "id": 1042,
    "name": "Flower Planting With No Adjacent",
    "slug": "flower-planting-with-no-adjacent",
    "category": "Graph",
    "aliases": [],
    "tags": ["greedy", "graph_coloring"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Assign one of four flower types to each garden such that no two adjacent gardens have the same flower type.",
}

def solve(flowerbed: list[int]) -> list[int]:
    """
    Assigns flower types to a flowerbed such that no two adjacent gardens 
    have the same flower type.

    The problem is a graph coloring problem where the graph is a cycle 
    (each garden is connected to its neighbors). Since the maximum degree 
    of any node in this graph is 2 (for a cycle) or 3 (if we consider 
    the input structure as a general graph, though here it's a simple cycle), 
    and we have 4 colors available, a greedy approach is guaranteed to work.

    Args:
        flowerbed: A list of integers representing the initial state of the gardens.
                   The input is guaranteed to be a valid cycle.

    Returns:
        A list of integers representing the flowerbed with assigned flower types.

    Examples:
        >>> solve([1, 2, 3, 4])
        [1, 2, 3, 4]
        >>> solve([1, 1, 1, 1])
        [1, 2, 3, 4]
    """
    n = len(flowerbed)
    # Create a copy to avoid mutating the input if that's a requirement, 
    # though here we return a new list.
    result = list(flowerbed)

    for i in range(n):
        # If the garden already has a flower, skip it.
        if result[i] != 0:
            continue

        # Identify the flower types used by neighbors.
        # We use modulo arithmetic to handle the circular nature of the garden.
        used_neighbors = set()
        
        # Check left neighbor
        left_neighbor_idx = (i - 1) % n
        if result[left_neighbor_idx] != 0:
            used_neighbors.add(result[left_neighbor_idx])
            
        # Check right neighbor
        right_neighbor_idx = (i + 1) % n
        if result[right_neighbor_idx] != 0:
            used_neighbors.add(result[right_neighbor_idx])

        # Greedy assignment: pick the first available flower type from {1, 2, 3, 4}
        # that is not in the used_neighbors set.
        for flower_type in range(1, 5):
            if flower_type not in used_neighbors:
                result[i] = flower_type
                break
                
    return result
