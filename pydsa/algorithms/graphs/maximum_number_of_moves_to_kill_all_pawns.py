METADATA = {
    "id": 3283,
    "name": "Maximum Number of Moves to Kill All Pawns",
    "slug": "maximum-number-of-moves-to-kill-all-pawns",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "bipartite_matching", "bfs"],
    "difficulty": "hard",
    "time_complexity": "O(N * E) where N is number of pawns and E is number of possible moves",
    "space_complexity": "O(N)",
    "description": "Find the maximum number of moves to kill all pawns where each move involves a pawn attacking an adjacent pawn of a different color.",
}

def solve(pawns: list[list[int]]) -> int:
    """
    Calculates the maximum number of moves to kill all pawns.
    
    The problem can be modeled as finding the maximum matching in a bipartite graph.
    Since pawns can only attack pawns of a different color, the graph is naturally 
    bipartite (Color A vs Color B). Each move removes two pawns (one attacker, one target).
    However, the problem asks for the maximum number of moves to kill *all* pawns.
    Actually, the problem is equivalent to finding the maximum matching in a graph 
    where edges exist between adjacent pawns of different colors.
    
    Wait, the problem states: "In one move, you can choose a pawn and an adjacent pawn 
    of a different color, and kill both." This is exactly the definition of 
    Maximum Bipartite Matching. Each match represents one move that kills two pawns.
    To kill as many pawns as possible, we maximize the number of pairs.
    
    Args:
        pawns: A list of [row, col] coordinates for each pawn.
        
    Returns:
        The maximum number of moves possible.
        
    Examples:
        >>> solve([[0,0], [0,1], [1,1], [1,0]])
        2
    """
    n = len(pawns)
    if n == 0:
        return 0

    # Separate pawns into two sets based on color (parity of row + col)
    # This ensures that adjacent pawns (dist=1) always belong to different sets.
    set_a = []
    set_b = []
    
    for i in range(n):
        r, c = pawns[i]
        if (r + c) % 2 == 0:
            set_a.append(i)
        else:
            set_b.append(i)
            
    # Build adjacency list: for each pawn in set_a, find adjacent pawns in set_b
    adj = {i: [] for i in set_a}
    pawn_coords = {i: (pawns[i][0], pawns[i][1]) for i in range(n)}
    
    # To speed up neighbor lookup, use a dictionary of coordinates
    coord_to_id = {pawn_coords[i]: i for i in range(n)}
    
    for i in set_a:
        r, c = pawn_coords[i]
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (r + dr, c + dc)
            if neighbor in coord_to_id:
                neighbor_id = coord_to_id[neighbor]
                # Only add edges to pawns in set_b
                if neighbor_id not in set_a:
                    adj[i].append(neighbor_id)

    # Standard Hopcroft-Karp or DFS-based augmenting path algorithm for Bipartite Matching
    match = {j: -1 for j in set_b}
    
    def can_match(u: int, visited: set[int]) -> bool:
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                # If v is not matched or we can find an augmenting path for its current match
                if match[v] < 0 or can_match(match[v], visited):
                    match[v] = u
                    return True
        return False

    matching_count = 0
    for i in set_a:
        if can_match(i, set()):
            matching_count += 1
            
    return matching_count
